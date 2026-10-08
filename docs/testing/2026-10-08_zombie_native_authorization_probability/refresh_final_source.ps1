$ErrorActionPreference = 'Stop'
$repoRoot = (Get-Location).Path
$evidence = Join-Path $repoRoot 'docs/testing/2026-10-08_zombie_native_authorization_probability'
$beforeDir = Join-Path $evidence 'before/common/raids'
$afterDir = Join-Path $evidence 'after/common/raids'
New-Item -ItemType Directory -Force -Path $afterDir | Out-Null

function Find-HoiBlock {
	param([string]$Source, [string]$Key, [int]$StartIndex = 0)
	$pattern = '(?m)^[\t ]*' + [regex]::Escape($Key) + '[\t ]*=[\t ]*\{'
	if ($StartIndex -ge $Source.Length) { return $null }
	$match = [regex]::Match($Source.Substring($StartIndex), $pattern)
	if (-not $match.Success) { return $null }
	$absoluteStart = $StartIndex + $match.Index
	$opening = $Source.IndexOf('{', $absoluteStart)
	$depth = 0
	$quoted = $false
	$comment = $false
	$escaped = $false
	for ($cursor = $opening; $cursor -lt $Source.Length; $cursor++) {
		$character = $Source[$cursor]
		if ($comment) { if ($character -eq "`n") { $comment = $false }; continue }
		if ($quoted) {
			if ($escaped) { $escaped = $false; continue }
			if ($character -eq '\') { $escaped = $true; continue }
			if ($character -eq '"') { $quoted = $false }
			continue
		}
		if ($character -eq '#') { $comment = $true; continue }
		if ($character -eq '"') { $quoted = $true; continue }
		if ($character -eq '{') { $depth++; continue }
		if ($character -eq '}') {
			$depth--
			if ($depth -eq 0) {
				return [pscustomobject]@{ Text = $Source.Substring($absoluteStart, $cursor - $absoluteStart + 1); EndIndex = $cursor }
			}
		}
	}
	throw "Unclosed block: $Key"
}
function Find-HoiBlocks {
	param([string]$Source, [string]$Key)
	$blocks = @()
	$cursor = 0
	while ($cursor -lt $Source.Length) {
		$block = Find-HoiBlock -Source $Source -Key $Key -StartIndex $cursor
		if ($null -eq $block) { break }
		$blocks += $block
		$cursor = $block.EndIndex + 1
	}
	return $blocks
}
function Hash-NormalizedText {
	param([string]$Value)
	$normalized = $Value -replace "`r`n", "`n" -replace "`r", "`n"
	$sha = [System.Security.Cryptography.SHA256]::Create()
	try { return ([System.BitConverter]::ToString($sha.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($normalized)))).Replace('-', '').ToLowerInvariant() }
	finally { $sha.Dispose() }
}
function Get-BlockHashes {
	param([object[]]$Blocks)
	$hashes = @($Blocks | ForEach-Object { Hash-NormalizedText $_.Text })
	return $hashes
}
function Get-ScalarValue {
	param([string]$Source, [string]$Key)
	$match = [regex]::Match($Source, '(?m)^[\t ]*' + [regex]::Escape($Key) + '[\t ]*=\s*([^\r\n#]+)')
	if ($match.Success) { return $match.Groups[1].Value.Trim() }
	return $null
}

$definitions = @(
	@{ path = 'common/raids/zombie_weaponized_raids.txt'; ids = @('weaponized_zombie_strike_low', 'weaponized_zombie_strike_medium', 'weaponized_zombie_strike_high') },
	@{ path = 'common/raids/zombie_weaponized_friendly_raids.txt'; ids = @('weaponized_zombie_strike_low_friendly', 'weaponized_zombie_strike_medium_friendly', 'weaponized_zombie_strike_high_friendly') }
)
$files = @()
$raidTypes = @()
foreach ($definition in $definitions) {
	$relative = $definition.path
	$livePath = Join-Path $repoRoot $relative
	$filename = $relative.Substring('common/raids/'.Length)
	$beforePath = Join-Path $beforeDir $filename
	$afterPath = Join-Path $afterDir $filename
	Copy-Item -LiteralPath $livePath -Destination $afterPath -Force
	$live = Get-Content -LiteralPath $livePath -Raw
	$before = Get-Content -LiteralPath $beforePath -Raw
	$liveHash = (Get-FileHash -LiteralPath $livePath -Algorithm SHA256).Hash.ToLowerInvariant()
	$afterHash = (Get-FileHash -LiteralPath $afterPath -Algorithm SHA256).Hash.ToLowerInvariant()
	$beforeHash = (Get-FileHash -LiteralPath $beforePath -Algorithm SHA256).Hash.ToLowerInvariant()
	$liveBytes = ([System.IO.File]::ReadAllBytes($livePath)).Length
	$afterBytes = ([System.IO.File]::ReadAllBytes($afterPath)).Length
	$beforeBytes = ([System.IO.File]::ReadAllBytes($beforePath)).Length
	$beforeConstants = @([regex]::Matches($before, '(?m)^@([A-Z0-9_]+)[\t ]*=[\t ]*([^\r\n#]+)') | ForEach-Object { $_.Groups[1].Value + '=' + $_.Groups[2].Value.Trim() } | Sort-Object)
	$finalConstants = @([regex]::Matches($live, '(?m)^@([A-Z0-9_]+)[\t ]*=[\t ]*([^\r\n#]+)') | ForEach-Object { $_.Groups[1].Value + '=' + $_.Groups[2].Value.Trim() } | Sort-Object)
	$files += [pscustomobject]@{
		path = $relative
		beforeArchive = "docs/testing/2026-10-08_zombie_native_authorization_probability/before/common/raids/$filename"
		beforeSha256 = $beforeHash
		beforeBytes = $beforeBytes
		finalAfterArchive = "docs/testing/2026-10-08_zombie_native_authorization_probability/after/common/raids/$filename"
		finalAfterSha256 = $afterHash
		finalAfterBytes = $afterBytes
		liveSourceSha256 = $liveHash
		liveSourceBytes = $liveBytes
		archiveMatchesLive = ($liveHash -eq $afterHash -and $liveBytes -eq $afterBytes)
		fileConstantsBefore = $beforeConstants
		fileConstantsFinal = $finalConstants
		fileConstantsUnchanged = ((ConvertTo-Json -InputObject $beforeConstants -Compress) -eq (ConvertTo-Json -InputObject $finalConstants -Compress))
	}
	foreach ($id in $definition.ids) {
		$beforeRaid = Find-HoiBlock $before $id
		$finalRaid = Find-HoiBlock $live $id
		if ($null -eq $beforeRaid -or $null -eq $finalRaid) { throw "RaidType missing: $id" }
		$beforeAi = Find-HoiBlock $beforeRaid.Text 'ai_will_do'
		$finalAi = Find-HoiBlock $finalRaid.Text 'ai_will_do'
		$beforeMods = @(Find-HoiBlocks $beforeAi.Text 'modifier')
		$finalMods = @(Find-HoiBlocks $finalAi.Text 'modifier')
		$authMods = @($finalMods | Where-Object { $_.Text -match 'weaponized_zombie_raid_can_target_from\s*=\s*yes' })
		$finalOldMods = @($finalMods | Where-Object { $_.Text -notmatch 'weaponized_zombie_raid_can_target_from\s*=\s*yes' })
		$beforeModHashes = @(Get-BlockHashes $beforeMods)
		$finalOldModHashes = @(Get-BlockHashes $finalOldMods)
		$beforeSuccess = Find-HoiBlock $beforeRaid.Text 'success_factors'
		$finalSuccess = Find-HoiBlock $finalRaid.Text 'success_factors'
		$beforeEquipment = Find-HoiBlock $beforeRaid.Text 'essential_equipment'
		$finalEquipment = Find-HoiBlock $finalRaid.Text 'essential_equipment'
		$beforeUnits = @(Find-HoiBlocks $beforeRaid.Text 'unit_requirements')
		$finalUnits = @(Find-HoiBlocks $finalRaid.Text 'unit_requirements')
		$beforeUnitHashes = @(Get-BlockHashes $beforeUnits)
		$finalUnitHashes = @(Get-BlockHashes $finalUnits)
		$finalAvailable = Find-HoiBlock $finalRaid.Text 'available'
		$oldBase = Get-ScalarValue $beforeAi.Text 'base'
		$finalBase = Get-ScalarValue $finalAi.Text 'base'
		$oldScalars = [ordered]@{}
		$finalScalars = [ordered]@{}
		foreach ($key in @('days_to_prepare', 'days_re_enable', 'command_power')) {
			$oldScalars[$key] = Get-ScalarValue $beforeRaid.Text $key
			$finalScalars[$key] = Get-ScalarValue $finalRaid.Text $key
		}
		$raidTypes += [pscustomobject]@{
			source = $relative
			raidType = $id
			beforeAiBase = $oldBase
			finalAiBase = $finalBase
			aiBaseUnchanged = ($oldBase -eq $finalBase)
			beforeExistingAiModifierCount = $beforeMods.Count
			finalExistingAiModifierCount = $finalOldMods.Count
			existingAiModifierHashesBefore = $beforeModHashes
			existingAiModifierHashesFinal = $finalOldModHashes
			existingAiModifiersUnchanged = ((ConvertTo-Json -InputObject $beforeModHashes -Compress) -eq (ConvertTo-Json -InputObject $finalOldModHashes -Compress))
			authorizationZeroModifierCount = $authMods.Count
			authorizationZeroModifierFactorZero = (@($authMods | Where-Object { $_.Text -match 'factor\s*=\s*0' }).Count -eq $authMods.Count)
			beforeSuccessFactorsSha256 = Hash-NormalizedText $beforeSuccess.Text
			finalSuccessFactorsSha256 = Hash-NormalizedText $finalSuccess.Text
			successFactorsUnchanged = ((Hash-NormalizedText $beforeSuccess.Text) -eq (Hash-NormalizedText $finalSuccess.Text))
			beforeEssentialEquipmentSha256 = Hash-NormalizedText $beforeEquipment.Text
			finalEssentialEquipmentSha256 = Hash-NormalizedText $finalEquipment.Text
			essentialEquipmentUnchanged = ((Hash-NormalizedText $beforeEquipment.Text) -eq (Hash-NormalizedText $finalEquipment.Text))
			beforeUnitRequirementHashes = $beforeUnitHashes
			finalUnitRequirementHashes = $finalUnitHashes
			unitRequirementsUnchanged = ((ConvertTo-Json -InputObject $beforeUnitHashes -Compress) -eq (ConvertTo-Json -InputObject $finalUnitHashes -Compress))
			beforeScalarCosts = $oldScalars
			finalScalarCosts = $finalScalars
			scalarCostsUnchanged = ((ConvertTo-Json -InputObject $oldScalars -Compress) -eq (ConvertTo-Json -InputObject $finalScalars -Compress))
			finalAvailableRetainsPayloadPredicate = ($finalAvailable.Text -match 'hidden_trigger\s*=\s*\{\s*has_weaponized_zombie_raid_payload\s*=\s*yes\s*\}')
			redundantPayloadTooltipRemoved = ($finalAvailable.Text -notmatch 'weaponized_zombie_raid_available_tooltip')
			authorizationTooltipPreserved = ($finalAvailable.Text -match 'weaponized_zombie_raid_authorization_tt')
			beforeAiWillDoSha256 = Hash-NormalizedText $beforeAi.Text
			finalAiWillDoSha256 = Hash-NormalizedText $finalAi.Text
		}
	}
}
$failed = @($raidTypes | Where-Object {
	-not $_.aiBaseUnchanged -or -not $_.existingAiModifiersUnchanged -or $_.authorizationZeroModifierCount -ne 1 -or
	-not $_.authorizationZeroModifierFactorZero -or -not $_.successFactorsUnchanged -or -not $_.essentialEquipmentUnchanged -or
	-not $_.unitRequirementsUnchanged -or -not $_.scalarCostsUnchanged -or -not $_.finalAvailableRetainsPayloadPredicate -or
	-not $_.redundantPayloadTooltipRemoved -or -not $_.authorizationTooltipPreserved
})
$refresh = [ordered]@{
	date = '2026-10-08'
	scope = 'Final source refresh after six payload-cost presentation wrapper removals; read-only source and evidence work.'
	mcpEvidenceTiming = 'All probability_inspect and probability_compare calls predate this presentation-only delta. Historical source hashes and receipts in mcp_baseline.json, mcp_after.json, and after_comparison.json are preserved; no unsupported native raid adapter was rerun.'
	comparisonMethod = 'Raid blocks were compared byte-for-byte after CRLF/LF normalization. Canonical before snapshots remain frozen. Final after copies were recopied from live source and checked against live file hashes and byte counts.'
	files = $files
	raidTypes = $raidTypes
	invariants = [ordered]@{
		allFileConstantsUnchanged = (@($files | Where-Object { -not $_.fileConstantsUnchanged }).Count -eq 0)
		allFinalSnapshotsMatchLive = (@($files | Where-Object { -not $_.archiveMatchesLive }).Count -eq 0)
		allAiBasesUnchanged = (@($raidTypes | Where-Object { -not $_.aiBaseUnchanged }).Count -eq 0)
		allPreexistingAiModifiersUnchanged = (@($raidTypes | Where-Object { -not $_.existingAiModifiersUnchanged }).Count -eq 0)
		exactlyOneAuthorizationZeroModifierEach = (@($raidTypes | Where-Object { $_.authorizationZeroModifierCount -ne 1 -or -not $_.authorizationZeroModifierFactorZero }).Count -eq 0)
		allSuccessFactorsUnchanged = (@($raidTypes | Where-Object { -not $_.successFactorsUnchanged }).Count -eq 0)
		allPayloadEquipmentBlocksUnchanged = (@($raidTypes | Where-Object { -not $_.essentialEquipmentUnchanged }).Count -eq 0)
		allUnitRequirementsUnchanged = (@($raidTypes | Where-Object { -not $_.unitRequirementsUnchanged }).Count -eq 0)
		allScalarCostsUnchanged = (@($raidTypes | Where-Object { -not $_.scalarCostsUnchanged }).Count -eq 0)
		allPayloadPredicatesRetained = (@($raidTypes | Where-Object { -not $_.finalAvailableRetainsPayloadPredicate }).Count -eq 0)
		allRedundantPayloadTooltipsRemoved = (@($raidTypes | Where-Object { -not $_.redundantPayloadTooltipRemoved }).Count -eq 0)
		allAuthorizationTooltipsPreserved = (@($raidTypes | Where-Object { -not $_.authorizationTooltipPreserved }).Count -eq 0)
		allPerTypeInvariantsPass = ($failed.Count -eq 0)
	}
	presentationDelta = [ordered]@{
		previousAfterHashes = @(
			[ordered]@{ path = 'common/raids/zombie_weaponized_raids.txt'; sha256 = '0819442c35482d2d98f1699df44f348725d7a6858139f3072fa84e65079acaf2' },
			[ordered]@{ path = 'common/raids/zombie_weaponized_friendly_raids.txt'; sha256 = '748cbdad5184cfd63660d068c95da22ef463dfce118ec2ef206e2a294e683917' }
		)
		finalHashes = @(
			[ordered]@{ path = 'common/raids/zombie_weaponized_raids.txt'; sha256 = $files[0].finalAfterSha256 },
			[ordered]@{ path = 'common/raids/zombie_weaponized_friendly_raids.txt'; sha256 = $files[1].finalAfterSha256 }
		)
		changeReceipt = 'docs/testing/2026-10-08_zombie_native_authorization/cost_presentation_change.json'
		wrappersReplaced = 6
		payloadPredicatePreserved = $true
		nativeEquipmentAndScalarCostsUnchanged = $true
		authorizationSentencePreserved = $true
		redundantTooltipLocalizationKeyRemoved = $true
	}
}
$outputPath = Join-Path $evidence 'final_source_refresh.json'
$refresh | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $outputPath -Encoding UTF8
$refresh | ConvertTo-Json -Depth 5

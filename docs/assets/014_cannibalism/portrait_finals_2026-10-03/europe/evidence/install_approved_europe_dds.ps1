$ErrorActionPreference = 'Stop'

$modRoot = (Get-Location).Path
$workspace = Join-Path $modRoot 'docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe'
$approvalPath = Join-Path $modRoot 'docs/plans/014_cannibalism_plans/evidence/2026-10-03_europe_portrait_parent_review.json'
$inventoryPath = Join-Path $workspace 'evidence/output_inventory.json'
$gfxPath = Join-Path $modRoot 'interface/014_cannibalism.gfx'
$charactersPath = Join-Path $modRoot 'common/characters/014_cannibalism_characters.txt'
$leaderDir = Join-Path $modRoot 'gfx/leaders/014_cannibalism'
$backupDir = Join-Path $workspace 'evidence/runtime_before'
$snapshotPath = Join-Path $workspace 'evidence/runtime_preinstall_snapshot.json'
$receiptPath = Join-Path $workspace 'evidence/runtime_install_receipt.json'

if (-not (Test-Path -LiteralPath $approvalPath)) { throw "Parent approval evidence missing: $approvalPath" }
if (Test-Path -LiteralPath $backupDir) { throw "Refusing to overwrite existing backup directory: $backupDir" }

$approval = Get-Content -Raw -LiteralPath $approvalPath | ConvertFrom-Json
$inventory = Get-Content -Raw -LiteralPath $inventoryPath | ConvertFrom-Json
if ($approval.rows.Count -ne 8 -or $approval.remaining_required_regional_finals -ne 48) { throw 'Parent review scope does not match the authorized eight-Europe / 48-remaining tranche.' }
if ($approval.acceptance_scope -notmatch '8Europeanoriginalfictionalfinalart' -or $approval.acceptance_scope -notmatch 'notfullevent/liveacceptance') { throw 'Parent evidence does not record the required bounded approval scope.' }
if ($approval.visual_review -notcontains 'decodedDDSnative8sheet') { throw 'Parent has not recorded final decoded-DDS contact-sheet review.' }
if (@($approval.rows | Where-Object { -not $_.png_pixels_equal }).Count -ne 0) { throw 'Parent review includes a failed selected PNG/DDS pixel comparison.' }
if ($inventory.GFX_and_runtime_crosswalk.Count -ne 8) { throw 'Local manifest crosswalk does not contain exactly eight approved rows.' }

$gfxLines = Get-Content -LiteralPath $gfxPath
$gfxEntries = @()
for ($i = 0; $i -lt $gfxLines.Count; $i++) {
    if ($gfxLines[$i] -match 'name = "(GFX_portrait_(CB[A-H])_warlord(?:_[a-z_]+)?)" texturefile = "([^"]+)"') {
        if ($Matches[3] -like 'gfx/leaders/014_cannibalism/leader_CB*_warlord*.dds') {
            $gfxEntries += [pscustomobject]@{ Line = $i + 1; Sprite = $Matches[1]; Slot = $Matches[2]; Path = $Matches[3] }
        }
    }
}
$uniqueGfxPaths = @($gfxEntries.Path | Sort-Object -Unique)
if ($uniqueGfxPaths.Count -ne 56) { throw "Expected 56 unique warlord DDS GFX paths, found $($uniqueGfxPaths.Count)." }

$parentByRuntime = @{}
foreach ($row in $approval.rows) { $parentByRuntime[$row.runtime] = $row }
$inventoryByRuntime = @{}
foreach ($row in $inventory.GFX_and_runtime_crosswalk) { $inventoryByRuntime[$row.runtime_dds_path] = $row }
if ($parentByRuntime.Count -ne 8) { throw 'Parent review runtime path set is not eight unique DDS paths.' }

$installRows = @()
foreach ($runtimeRel in $parentByRuntime.Keys) {
    $reviewRow = $parentByRuntime[$runtimeRel]
    $inventoryRow = $inventoryByRuntime[$runtimeRel]
    if ($null -eq $inventoryRow) { throw "Runtime path is absent from the inspected crosswalk: $runtimeRel" }
    if ($reviewRow.candidate -notmatch 'candidate_dds/(leader_CB[A-H]_warlord(?:_europe)?\.dds)$') { throw "Unexpected candidate DDS route: $($reviewRow.candidate)" }
    $candidatePath = Join-Path $modRoot ($reviewRow.candidate -replace '/', '\')
    $runtimePath = Join-Path $modRoot $runtimeRel
    if (-not (Test-Path -LiteralPath $candidatePath) -or -not (Test-Path -LiteralPath $runtimePath)) { throw "Missing candidate or runtime DDS for $runtimeRel" }
    $candidateHash = (Get-FileHash -LiteralPath $candidatePath -Algorithm SHA256).Hash
    if ($candidateHash -ne $reviewRow.candidate_sha256.ToUpperInvariant()) { throw "Candidate hash does not match parent-approved hash: $candidatePath" }
    if ($candidateHash -ne $inventoryRow.candidate_dds_sha256) { throw "Candidate hash does not match output inventory: $candidatePath" }
    $oldHash = (Get-FileHash -LiteralPath $runtimePath -Algorithm SHA256).Hash
    if ($oldHash -ne $reviewRow.runtime_before_sha256.ToUpperInvariant() -or $oldHash -ne $inventoryRow.runtime_dds_sha256_before) { throw "Existing runtime DDS does not match both recorded baselines: $runtimePath" }
    if ($reviewRow.png_pixels_equal -ne $true -or [string]::IsNullOrWhiteSpace($reviewRow.decoded_pixel_sha256)) { throw "Parent pixel review is incomplete for $runtimeRel" }

    $slot = [regex]::Match($runtimeRel, 'leader_(CB[A-H])_warlord').Groups[1].Value
    $expectedSprites = @("GFX_portrait_${slot}_warlord", "GFX_portrait_${slot}_warlord_europe")
    foreach ($sprite in $expectedSprites) {
        $spriteRows = @($gfxEntries | Where-Object { $_.Sprite -eq $sprite -and $_.Path -eq $runtimeRel })
        if ($spriteRows.Count -ne 1) { throw "GFX crosswalk mismatch for $sprite -> $runtimeRel" }
    }
    $installRows += [pscustomobject]@{ Slot = $slot; CandidatePath = $candidatePath; CandidateRelative = $reviewRow.candidate; CandidateHash = $candidateHash; RuntimePath = $runtimePath; RuntimeRelative = $runtimeRel; OldHash = $oldHash; ParentDecodedPixelHash = $reviewRow.decoded_pixel_sha256 }
}
if ($installRows.Count -ne 8 -or @($installRows.RuntimeRelative | Sort-Object -Unique).Count -ne 8) { throw 'Install route is not exactly eight unique Europe DDS paths.' }

$allDdsBefore = @(Get-ChildItem -LiteralPath $leaderDir -File -Filter '*.dds' | Sort-Object Name | ForEach-Object {
    [pscustomobject]@{ Path = "gfx/leaders/014_cannibalism/$($_.Name)"; Name = $_.Name; Bytes = $_.Length; SHA256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash }
})
if ($allDdsBefore.Count -ne 60) { throw "Expected 60 Event 014 leader DDS files before install, found $($allDdsBefore.Count)." }
$allowedSet = @{}
foreach ($row in $installRows) { $allowedSet[$row.RuntimeRelative.ToLowerInvariant()] = $true }
$otherBefore = @($allDdsBefore | Where-Object { -not $allowedSet[$_.Path.ToLowerInvariant()] })
if ($otherBefore.Count -ne 52) { throw "Expected 52 protected DDS files, found $($otherBefore.Count)." }

$protectedPaths = @($gfxPath, $charactersPath)
foreach ($name in @('hannibal.dds', 'hannibal_wendigo.dds', 'leader_CBL_hannibal_sheet.dds', 'leader_ZZZ_hannibal_wendigo_sheet.dds')) {
    $protectedPaths += Join-Path $leaderDir $name
}
$protectedBefore = @($protectedPaths | ForEach-Object {
    if (-not (Test-Path -LiteralPath $_)) { throw "Protected file missing: $_" }
    [pscustomobject]@{ Path = (Resolve-Path -LiteralPath $_).Path; Bytes = (Get-Item -LiteralPath $_).Length; SHA256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash }
})

New-Item -ItemType Directory -Path $backupDir | Out-Null
$backups = @()
foreach ($row in $installRows) {
    $backupPath = Join-Path $backupDir ([IO.Path]::GetFileName($row.RuntimePath))
    if (Test-Path -LiteralPath $backupPath) { throw "Refusing to overwrite backup: $backupPath" }
    Copy-Item -LiteralPath $row.RuntimePath -Destination $backupPath
    $backupHash = (Get-FileHash -LiteralPath $backupPath -Algorithm SHA256).Hash
    if ($backupHash -ne $row.OldHash) { throw "Backup hash mismatch for $($row.RuntimeRelative)" }
    $backups += [pscustomobject]@{ RuntimePath = $row.RuntimeRelative; BackupPath = "docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/evidence/runtime_before/$([IO.Path]::GetFileName($backupPath))"; Bytes = (Get-Item -LiteralPath $backupPath).Length; SHA256 = $backupHash; MatchesRecordedBaseline = $true }
}

$preSnapshot = [ordered]@{
    date = '2026-10-03'
    parent_review = 'docs/plans/014_cannibalism_plans/evidence/2026-10-03_europe_portrait_parent_review.json'
    total_event_leader_dds = $allDdsBefore.Count
    approved_install_targets = $installRows.Count
    protected_other_dds = $otherBefore.Count
    dds = $allDdsBefore
    gfx_and_character = $protectedBefore
    backups = $backups
}
[IO.File]::WriteAllText($snapshotPath, ($preSnapshot | ConvertTo-Json -Depth 8), [System.Text.UTF8Encoding]::new($false))

$installStarted = $false
try {
    foreach ($row in $installRows) {
        Copy-Item -LiteralPath $row.CandidatePath -Destination $row.RuntimePath -Force
        $installStarted = $true
    }

    $installed = @()
    foreach ($row in $installRows) {
        $actual = (Get-FileHash -LiteralPath $row.RuntimePath -Algorithm SHA256).Hash
        if ($actual -ne $row.CandidateHash) { throw "Installed hash does not match approved candidate for $($row.RuntimeRelative)" }
        $bytes = (Get-Item -LiteralPath $row.RuntimePath).Length
        if ($bytes -ne 131168) { throw "Unexpected installed DDS size for $($row.RuntimeRelative): $bytes" }
        $installed += [pscustomobject]@{ Slot = $row.Slot; RuntimePath = $row.RuntimeRelative; CandidatePath = $row.CandidateRelative; Bytes = $bytes; PreviousSHA256 = $row.OldHash; InstalledSHA256 = $actual; MatchesParentApprovedCandidate = $true }
    }

    $allDdsAfter = @(Get-ChildItem -LiteralPath $leaderDir -File -Filter '*.dds' | Sort-Object Name | ForEach-Object {
        [pscustomobject]@{ Path = "gfx/leaders/014_cannibalism/$($_.Name)"; Name = $_.Name; Bytes = $_.Length; SHA256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash }
    })
    if ($allDdsAfter.Count -ne 60) { throw "Event 014 leader DDS count changed after install: $($allDdsAfter.Count)" }
    $beforeByPath = @{}
    foreach ($item in $allDdsBefore) { $beforeByPath[$item.Path.ToLowerInvariant()] = $item }
    $afterByPath = @{}
    foreach ($item in $allDdsAfter) { $afterByPath[$item.Path.ToLowerInvariant()] = $item }
    $protectedDds = @()
    foreach ($before in $otherBefore) {
        $after = $afterByPath[$before.Path.ToLowerInvariant()]
        if ($null -eq $after -or $after.SHA256 -ne $before.SHA256 -or $after.Bytes -ne $before.Bytes) { throw "Protected Event 014 DDS changed: $($before.Path)" }
        $protectedDds += [pscustomobject]@{ Path = $before.Path; Bytes = $before.Bytes; SHA256Before = $before.SHA256; SHA256After = $after.SHA256; Unchanged = $true }
    }

    $protectedAfter = @($protectedPaths | ForEach-Object {
        [pscustomobject]@{ Path = (Resolve-Path -LiteralPath $_).Path; Bytes = (Get-Item -LiteralPath $_).Length; SHA256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash }
    })
    for ($i = 0; $i -lt $protectedBefore.Count; $i++) {
        if ($protectedBefore[$i].SHA256 -ne $protectedAfter[$i].SHA256 -or $protectedBefore[$i].Bytes -ne $protectedAfter[$i].Bytes) { throw "Protected GFX/character/Hannibal file changed: $($protectedBefore[$i].Path)" }
    }

    $receipt = [ordered]@{
        date = '2026-10-03'
        status = 'eight parent-approved Europe DDS files installed; runtime promotion limited to approved paths'
        parent_review = 'docs/plans/014_cannibalism_plans/evidence/2026-10-03_europe_portrait_parent_review.json'
        parent_acceptance_scope = $approval.acceptance_scope
        parent_reviewed_decoded_dds_contact_sheet = $true
        parent_verified_png_dds_rgba_equality_for_all_eight = $true
        selected_CBA_candidate = 'CBA-v02'
        user_authorized_new_art_decision = $false
        old_files_backed_up_under = 'docs/assets/014_cannibalism/portrait_finals_2026-10-03/europe/evidence/runtime_before/'
        backup_count = $backups.Count
        installed_count = $installed.Count
        total_event_leader_dds = $allDdsAfter.Count
        protected_other_dds_count = $protectedDds.Count
        protected_other_dds_unchanged = $true
        protected_gfx_character_hannibal_files_unchanged = $true
        modified_runtime_paths = @($installed | ForEach-Object { $_.RuntimePath })
        installed = $installed
        backups = $backups
        other_52_dds = $protectedDds
        protected_files = @($protectedBefore | ForEach-Object -Begin { $index = 0 } -Process {
            $before = $_
            $after = $protectedAfter[$index]
            $index++
            [pscustomobject]@{ Path = $before.Path; BytesBefore = $before.Bytes; BytesAfter = $after.Bytes; SHA256Before = $before.SHA256; SHA256After = $after.SHA256; Unchanged = $before.SHA256 -eq $after.SHA256 }
        })
        remaining_regional_portraits_queued = 48
        full_Event_014_portrait_goal_complete = $false
        no_GFX_or_character_reference_changes = $true
        no_commit = $true
    }
    [IO.File]::WriteAllText($receiptPath, ($receipt | ConvertTo-Json -Depth 10), [System.Text.UTF8Encoding]::new($false))
    Write-Output "INSTALL_OK targets=$($installed.Count) protected_dds=$($protectedDds.Count) protected_files=$($protectedAfter.Count) remaining_queued=48"
}
catch {
    if ($installStarted) {
        foreach ($backup in $backups) {
            $runtimePath = Join-Path $modRoot $backup.RuntimePath
            $backupPath = Join-Path $modRoot $backup.BackupPath
            Copy-Item -LiteralPath $backupPath -Destination $runtimePath -Force
        }
    }
    throw
}

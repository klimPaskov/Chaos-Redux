$ErrorActionPreference = "Stop"

$userScopedMeshyApiKey = [Environment]::GetEnvironmentVariable("MESHY_API_KEY", "User")
if (-not [string]::IsNullOrWhiteSpace($userScopedMeshyApiKey)) {
	$env:MESHY_API_KEY = $userScopedMeshyApiKey
}

if ([string]::IsNullOrWhiteSpace($env:MESHY_API_KEY)) {
	throw "MESHY_API_KEY is missing. Stop before starting Meshy."
}

$packageVersion = if ([string]::IsNullOrWhiteSpace($env:MESHY_MCP_VERSION)) { "0.4.0" } else { $env:MESHY_MCP_VERSION }
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..")).Path
$dependencyLockPath = Join-Path $repoRoot ".tools\3d_pipeline\config\dependencies.lock.json"
$dependencyLock = Get-Content -LiteralPath $dependencyLockPath -Raw | ConvertFrom-Json
$sdkVersion = $dependencyLock.routes.meshy_mcp.resolved_dependencies.modelcontextprotocol_sdk.version
if ([string]::IsNullOrWhiteSpace($sdkVersion)) {
	throw "The dependency lock does not define the Meshy MCP SDK compatibility version."
}
$runtimeVersionSlug = $packageVersion.Replace(".", "_")
$sdkVersionSlug = $sdkVersion.Replace(".", "_")
$runtimeRoot = Join-Path $repoRoot ".tmp\meshy_mcp_compat_v4_${runtimeVersionSlug}_sdk_$sdkVersionSlug"
$packageRoot = Join-Path $runtimeRoot "node_modules\@meshy-ai\meshy-mcp-server"
$manifestPath = Join-Path $packageRoot "package.json"
$sdkManifestPath = Join-Path $runtimeRoot "node_modules\@modelcontextprotocol\sdk\package.json"
$sdkServerEntryPath = Join-Path $runtimeRoot "node_modules\@modelcontextprotocol\sdk\dist\esm\server\index.js"
$sdkStreamableHttpPath = Join-Path $runtimeRoot "node_modules\@modelcontextprotocol\sdk\dist\esm\server\streamableHttp.js"

$npmExe = "C:\Program Files\nodejs\npm.cmd"
if (-not (Test-Path -LiteralPath $npmExe)) {
	$npmExe = (Get-Command npm.cmd -ErrorAction Stop).Source
}
$nodeExe = "C:\Program Files\nodejs\node.exe"
if (-not (Test-Path -LiteralPath $nodeExe)) {
	$nodeExe = (Get-Command node.exe -ErrorAction Stop).Source
}

$runtimeMutexName = "Local\ChaosReduxMeshyMcpCompat_${runtimeVersionSlug}_sdk_$sdkVersionSlug"
$runtimeMutex = [System.Threading.Mutex]::new($false, $runtimeMutexName)
$runtimeMutexHeld = $false
try {
	try {
		$runtimeMutexHeld = $runtimeMutex.WaitOne([TimeSpan]::FromMinutes(5))
	}
	catch [System.Threading.AbandonedMutexException] {
		$runtimeMutexHeld = $true
	}
	if (-not $runtimeMutexHeld) {
		throw "Timed out waiting for the locked Meshy MCP compatibility runtime."
	}

$installedVersion = $null
if (Test-Path -LiteralPath $manifestPath) {
	$installedVersion = (Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json).version
}
$installedSdkVersion = $null
if (Test-Path -LiteralPath $sdkManifestPath) {
	$installedSdkVersion = (Get-Content -LiteralPath $sdkManifestPath -Raw | ConvertFrom-Json).version
}
if (
	$installedVersion -ne $packageVersion -or
	$installedSdkVersion -ne $sdkVersion -or
	-not (Test-Path -LiteralPath $sdkServerEntryPath) -or
	-not (Test-Path -LiteralPath $sdkStreamableHttpPath)
) {
	New-Item -ItemType Directory -Force -Path $runtimeRoot | Out-Null
	& $npmExe install --prefix $runtimeRoot --no-save --save-exact --force "@meshy-ai/meshy-mcp-server@$packageVersion" "@modelcontextprotocol/sdk@$sdkVersion" | Out-Null
	if ($LASTEXITCODE -ne 0) {
		throw "Failed to install @meshy-ai/meshy-mcp-server@$packageVersion with @modelcontextprotocol/sdk@$sdkVersion."
	}
	if (
		-not (Test-Path -LiteralPath $sdkServerEntryPath) -or
		-not (Test-Path -LiteralPath $sdkStreamableHttpPath)
	) {
		throw "The reconstructed Meshy MCP compatibility runtime is missing a locked SDK server entry point."
	}
}

$constantsPath = Join-Path $packageRoot "dist\constants.js"
$constantsTypesPath = Join-Path $packageRoot "dist\constants.d.ts"
$generationToolPath = Join-Path $packageRoot "dist\tools\generation.js"
$generationSchemaPath = Join-Path $packageRoot "dist\schemas\generation.js"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$constantsText = [System.IO.File]::ReadAllText($constantsPath, $utf8NoBom)
$constantsPattern = '(?ms)(export var AIModel;\s*\(function \(AIModel\) \{\s*).*?(\s*\}\)\(AIModel \|\| \(AIModel = \{\}\)\);)'
$constantsMatch = [regex]::Match($constantsText, $constantsPattern)
if (-not $constantsMatch.Success) {
	throw "Meshy MCP AI model constants no longer match the compatibility wrapper."
}
$constantsReplacement = 'export var AIModel;' + "`n" + '(function (AIModel) {' + "`n" + '    AIModel["MESHY_7"] = "meshy-7";' + "`n" + '    AIModel["LATEST"] = "latest";' + "`n" + '})(AIModel || (AIModel = {}));'
$constantsText = $constantsText.Remove($constantsMatch.Index, $constantsMatch.Length).Insert($constantsMatch.Index, $constantsReplacement)
[System.IO.File]::WriteAllText($constantsPath, $constantsText, $utf8NoBom)

$constantsTypesText = [System.IO.File]::ReadAllText($constantsTypesPath, $utf8NoBom)
$constantsTypesPattern = '(?ms)(export declare enum AIModel \{\s*).*?(\s*\})'
$constantsTypesMatch = [regex]::Match($constantsTypesText, $constantsTypesPattern)
if (-not $constantsTypesMatch.Success) {
	throw "Meshy MCP AI model type declaration no longer matches the compatibility wrapper."
}
$constantsTypesReplacement = 'export declare enum AIModel {' + "`n" + '    MESHY_7 = "meshy-7",' + "`n" + '    LATEST = "latest"' + "`n" + '}'
$constantsTypesText = $constantsTypesText.Remove($constantsTypesMatch.Index, $constantsTypesMatch.Length).Insert($constantsTypesMatch.Index, $constantsTypesReplacement)
[System.IO.File]::WriteAllText($constantsTypesPath, $constantsTypesText, $utf8NoBom)

$toolText = [System.IO.File]::ReadAllText($generationToolPath, $utf8NoBom)
$gatePattern = '(?ms)            // (?:hd_texture|Meshy).*?            if \(params\.save_pre_remeshed_model'
$gateReplacement = @'
            // Meshy 7 accepts image enhancement. Lighting removal is omitted
            // because it is not part of the Meshy 7 image-to-3D request.
            const isMeshy7Image = params.ai_model === "meshy-7" || params.ai_model === "latest" || !params.ai_model;
            if (isMeshy7Image) {
                if (params.hd_texture !== undefined) {
                    request.hd_texture = params.hd_texture;
                }
                if (params.image_enhancement !== undefined) {
                    request.image_enhancement = params.image_enhancement;
                }
            }
            if (params.save_pre_remeshed_model
'@
$gateMatch = [regex]::Match($toolText, $gatePattern)
if (-not $gateMatch.Success) {
	throw "Meshy MCP image-to-3D parameter gate no longer matches the compatibility wrapper."
}
$normalizedGate = $gateReplacement.TrimStart("`r", "`n")
$toolText = $toolText.Remove($gateMatch.Index, $gateMatch.Length).Insert($gateMatch.Index, $normalizedGate)
$toolText = [regex]::Replace($toolText, 'meshy-\d+', 'meshy-7')
$toolText = $toolText.Replace('"meshy-7", "meshy-7", "meshy-7"', '"meshy-7"')
[System.IO.File]::WriteAllText($generationToolPath, $toolText, $utf8NoBom)

$schemaText = [System.IO.File]::ReadAllText($generationSchemaPath, $utf8NoBom)
$schemaText = [regex]::Replace($schemaText, 'meshy-\d+', 'meshy-7')
$schemaText = $schemaText.Replace("'meshy-7', 'meshy-7', or 'latest'", "'meshy-7'")
$schemaText = $schemaText.Replace("'meshy-7', 'meshy-7', 'meshy-7', or 'latest'", "'meshy-7'")
[System.IO.File]::WriteAllText($generationSchemaPath, $schemaText, $utf8NoBom)

Get-ChildItem -LiteralPath (Join-Path $packageRoot "dist") -Recurse -Filter "*.js" | ForEach-Object {
	$runtimeText = [System.IO.File]::ReadAllText($_.FullName, $utf8NoBom)
	$runtimeText = [regex]::Replace($runtimeText, '(?i)meshy-\d+', 'meshy-7')
	$runtimeText = [regex]::Replace($runtimeText, 'Meshy \d+', 'Meshy 7')
	[System.IO.File]::WriteAllText($_.FullName, $runtimeText, $utf8NoBom)
}

if ((Get-Item -LiteralPath $generationToolPath).Length -gt 5MB) {
	throw "Meshy MCP compatibility output exceeded the safe size limit. Refusing to start the route."
}
}
finally {
	if ($runtimeMutexHeld) {
		$runtimeMutex.ReleaseMutex()
	}
	$runtimeMutex.Dispose()
}

$entryPoint = Join-Path $packageRoot "dist\index.js"
& $nodeExe $entryPoint
exit $LASTEXITCODE

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($env:MESHY_API_KEY)) {
	throw "MESHY_API_KEY is missing. Stop before starting Meshy."
}

$packageVersion = if ([string]::IsNullOrWhiteSpace($env:MESHY_MCP_VERSION)) { "0.4.0" } else { $env:MESHY_MCP_VERSION }
$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..")).Path
$runtimeVersionSlug = $packageVersion.Replace(".", "_")
$runtimeRoot = Join-Path $repoRoot ".tmp\meshy_mcp_compat_v4_$runtimeVersionSlug"
$packageRoot = Join-Path $runtimeRoot "node_modules\@meshy-ai\meshy-mcp-server"
$manifestPath = Join-Path $packageRoot "package.json"
$sdkManifestPath = Join-Path $runtimeRoot "node_modules\@modelcontextprotocol\sdk\package.json"
$honoManifestPath = Join-Path $runtimeRoot "node_modules\hono\package.json"

$npmExe = "C:\Program Files\nodejs\npm.cmd"
if (-not (Test-Path -LiteralPath $npmExe)) {
	$npmExe = (Get-Command npm.cmd -ErrorAction Stop).Source
}
$nodeExe = "C:\Program Files\nodejs\node.exe"
if (-not (Test-Path -LiteralPath $nodeExe)) {
	$nodeExe = (Get-Command node.exe -ErrorAction Stop).Source
}

$installedVersion = $null
if (Test-Path -LiteralPath $manifestPath) {
	$installedVersion = (Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json).version
}
if (
	$installedVersion -ne $packageVersion -or
	-not (Test-Path -LiteralPath $sdkManifestPath) -or
	-not (Test-Path -LiteralPath $honoManifestPath)
) {
	New-Item -ItemType Directory -Force -Path $runtimeRoot | Out-Null
	& $npmExe install --prefix $runtimeRoot --no-save "@meshy-ai/meshy-mcp-server@$packageVersion" | Out-Null
	if ($LASTEXITCODE -ne 0) {
		throw "Failed to install @meshy-ai/meshy-mcp-server@$packageVersion."
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
$toolText = [regex]::Replace($toolText, 'meshy-[0-6]', 'meshy-7')
$toolText = $toolText.Replace('"meshy-7", "meshy-7", "meshy-7"', '"meshy-7"')
[System.IO.File]::WriteAllText($generationToolPath, $toolText, $utf8NoBom)

$schemaText = [System.IO.File]::ReadAllText($generationSchemaPath, $utf8NoBom)
$schemaText = [regex]::Replace($schemaText, 'meshy-[0-6]', 'meshy-7')
$schemaText = $schemaText.Replace("'meshy-7', 'meshy-7', or 'latest'", "'meshy-7'")
$schemaText = $schemaText.Replace("'meshy-7', 'meshy-7', 'meshy-7', or 'latest'", "'meshy-7'")
[System.IO.File]::WriteAllText($generationSchemaPath, $schemaText, $utf8NoBom)

Get-ChildItem -LiteralPath (Join-Path $packageRoot "dist") -Recurse -Filter "*.js" | ForEach-Object {
	$runtimeText = [System.IO.File]::ReadAllText($_.FullName, $utf8NoBom)
	$runtimeText = [regex]::Replace($runtimeText, '(?i)meshy-[0-6]', 'meshy-7')
	$runtimeText = [regex]::Replace($runtimeText, 'Meshy [0-6]', 'Meshy 7')
	[System.IO.File]::WriteAllText($_.FullName, $runtimeText, $utf8NoBom)
}

if ((Get-Item -LiteralPath $generationToolPath).Length -gt 5MB) {
	throw "Meshy MCP compatibility output exceeded the safe size limit. Refusing to start the route."
}

$entryPoint = Join-Path $packageRoot "dist\index.js"
& $nodeExe $entryPoint
exit $LASTEXITCODE

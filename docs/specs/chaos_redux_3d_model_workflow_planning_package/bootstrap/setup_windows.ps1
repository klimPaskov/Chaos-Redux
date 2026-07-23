[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)]
    [string]$RepoRoot,

    [Parameter(Mandatory = $true)]
    [string]$BlenderExe,

    [string]$DependencyLock = ".tools\3d_pipeline\config\dependencies.lock.json",
    [string]$ProjectMcpTemplate = ".tools\3d_pipeline\config\codex_mcp.example.toml",
    [string]$ProjectMcpDestination,
    [string]$PdxZip,
    [string]$PdxSha256,
    [string]$BlenderMcpZip,
    [string]$BlenderMcpSha256,
    [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-RepoPath {
    param([string]$Path)
    if ([System.IO.Path]::IsPathRooted($Path)) {
        return $Path
    }
    return Join-Path $RepoRoot $Path
}

function Get-CommandSummary {
    param([string]$Name, [string[]]$VersionArgs = @("--version"))
    $command = Get-Command $Name -ErrorAction SilentlyContinue
    if ($null -eq $command) {
        return [ordered]@{ name = $Name; found = $false; path = $null; version = $null }
    }
    $version = $null
    try {
        $version = (& $command.Source @VersionArgs 2>&1 | Select-Object -First 1 | Out-String).Trim()
    } catch {
        $version = "version query failed: $($_.Exception.Message)"
    }
    return [ordered]@{ name = $Name; found = $true; path = $command.Source; version = $version }
}

if (-not (Test-Path -LiteralPath $RepoRoot -PathType Container)) {
    throw "Repository root does not exist: $RepoRoot"
}
if (-not (Test-Path -LiteralPath $BlenderExe -PathType Leaf)) {
    throw "Blender executable does not exist: $BlenderExe"
}

$resolvedLock = Resolve-RepoPath $DependencyLock
$resolvedTemplate = Resolve-RepoPath $ProjectMcpTemplate

Write-Host "Chaos Redux 3D pipeline workstation discovery"
Write-Host "Repository: $RepoRoot"
Write-Host "Blender: $BlenderExe"

$tools = @(
    (Get-CommandSummary -Name "node")
    (Get-CommandSummary -Name "npm")
    (Get-CommandSummary -Name "npx")
    (Get-CommandSummary -Name "python")
    (Get-CommandSummary -Name "uv")
)
$tools | ForEach-Object {
    Write-Host ("{0}: found={1} path={2} version={3}" -f $_.name, $_.found, $_.path, $_.version)
}

$blenderVersion = (& $BlenderExe --version 2>&1 | Select-Object -First 1 | Out-String).Trim()
Write-Host "Blender version: $blenderVersion"
Write-Host "MESHY_API_KEY present: $(-not [string]::IsNullOrWhiteSpace($env:MESHY_API_KEY))"

if (-not (Test-Path -LiteralPath $resolvedLock -PathType Leaf)) {
    Write-Warning "Dependency lock was not found: $resolvedLock"
} else {
    $lock = Get-Content -LiteralPath $resolvedLock -Raw | ConvertFrom-Json
    Write-Host "Dependency lock status: $($lock.status)"
    $unapproved = @($lock.dependencies | Where-Object { -not $_.approved })
    if ($unapproved.Count -gt 0) {
        Write-Warning "Dependency lock has $($unapproved.Count) unapproved entries. Installation must not be promoted."
    }
}

$requiredDirectories = @(
    ".tools\3d_pipeline\blender_profile\config",
    ".tools\3d_pipeline\blender_profile\scripts",
    ".tools\3d_pipeline\blender_profile\extensions",
    ".tools\3d_pipeline\blender_profile\cache",
    ".tools\3d_pipeline\reports",
    ".tools\3d_pipeline\logs"
)

foreach ($relative in $requiredDirectories) {
    $path = Join-Path $RepoRoot $relative
    Write-Host "Directory: $path"
    if ($Apply -and $PSCmdlet.ShouldProcess($path, "Create directory")) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

if (-not [string]::IsNullOrWhiteSpace($ProjectMcpDestination)) {
    if (-not (Test-Path -LiteralPath $resolvedTemplate -PathType Leaf)) {
        throw "MCP template does not exist: $resolvedTemplate"
    }
    Write-Host "MCP template copy: $resolvedTemplate -> $ProjectMcpDestination"
    if ($Apply -and $PSCmdlet.ShouldProcess($ProjectMcpDestination, "Write project MCP configuration template")) {
        if (Test-Path -LiteralPath $ProjectMcpDestination) {
            $backup = "$ProjectMcpDestination.$((Get-Date).ToString('yyyyMMdd_HHmmss')).bak"
            Copy-Item -LiteralPath $ProjectMcpDestination -Destination $backup
            Write-Host "Existing MCP configuration backed up to $backup"
        }
        Copy-Item -LiteralPath $resolvedTemplate -Destination $ProjectMcpDestination
        Write-Host "Review and replace all placeholder paths before starting MCP servers."
    }
}

if (-not [string]::IsNullOrWhiteSpace($PdxZip) -or -not [string]::IsNullOrWhiteSpace($BlenderMcpZip)) {
    $installer = Join-Path $PSScriptRoot "install_blender_extensions.ps1"
    & $installer `
        -BlenderExe $BlenderExe `
        -PdxZip $PdxZip `
        -PdxSha256 $PdxSha256 `
        -BlenderMcpZip $BlenderMcpZip `
        -BlenderMcpSha256 $BlenderMcpSha256 `
        -Apply:$Apply
}

if (-not $Apply) {
    Write-Host "Discovery complete. No changes were made. Review warnings and rerun with -Apply only after the dependency lock is approved."
} else {
    Write-Host "Setup actions complete. Run verify_environment.ps1. This script does not mark the environment production-ready."
}

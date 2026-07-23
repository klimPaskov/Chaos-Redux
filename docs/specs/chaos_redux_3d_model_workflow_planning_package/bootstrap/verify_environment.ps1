[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$RepoRoot,

    [Parameter(Mandatory = $true)]
    [string]$BlenderExe,

    [string]$DependencyLock = ".tools\3d_pipeline\config\dependencies.lock.json",
    [string]$OutputPath = ".tools\3d_pipeline\reports\environment.json",
    [int[]]$ForbiddenNonLoopbackPorts = @(9876, 3000)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Resolve-RepoPath {
    param([string]$Path)
    if ([System.IO.Path]::IsPathRooted($Path)) { return $Path }
    return Join-Path $RepoRoot $Path
}

function Test-Tool {
    param([string]$Name)
    $cmd = Get-Command $Name -ErrorAction SilentlyContinue
    if ($null -eq $cmd) {
        return [ordered]@{ found = $false; path = $null; version = $null }
    }
    $version = $null
    try { $version = (& $cmd.Source --version 2>&1 | Select-Object -First 1 | Out-String).Trim() } catch { $version = $_.Exception.Message }
    return [ordered]@{ found = $true; path = $cmd.Source; version = $version }
}

$checks = New-Object System.Collections.Generic.List[object]
function Add-Check {
    param([string]$Name, [bool]$Passed, [string]$Detail, [string]$Severity = "blocker")
    $checks.Add([ordered]@{ name = $Name; passed = $Passed; detail = $Detail; severity = $Severity })
}

Add-Check -Name "repo_root" -Passed (Test-Path -LiteralPath $RepoRoot -PathType Container) -Detail $RepoRoot
Add-Check -Name "blender_executable" -Passed (Test-Path -LiteralPath $BlenderExe -PathType Leaf) -Detail $BlenderExe

$node = Test-Tool "node"
$npx = Test-Tool "npx"
$python = Test-Tool "python"
$uv = Test-Tool "uv"
Add-Check -Name "node" -Passed $node.found -Detail ($node | ConvertTo-Json -Compress)
Add-Check -Name "npx" -Passed $npx.found -Detail ($npx | ConvertTo-Json -Compress)
Add-Check -Name "python" -Passed $python.found -Detail ($python | ConvertTo-Json -Compress)
Add-Check -Name "uv" -Passed $uv.found -Detail ($uv | ConvertTo-Json -Compress) -Severity "major"
Add-Check -Name "meshy_api_key_present" -Passed (-not [string]::IsNullOrWhiteSpace($env:MESHY_API_KEY)) -Detail "Key value is intentionally not reported."

if ([string]::IsNullOrWhiteSpace($env:MESHY_API_KEY)) {
    Write-Host "Meshy start gate failed. `MESHY_API_KEY` is missing." -ForegroundColor Red
    Write-Host "Run this PowerShell command, then restart the shell or Codex:" -ForegroundColor Yellow
    Write-Host @'
[Environment]::SetEnvironmentVariable(
    "MESHY_API_KEY",
    "msy_your_actual_key_here",
    "User"
)
'@
    Write-Host "PowerShell command to set MESHY_API_KEY shown above." -ForegroundColor Yellow
}

$blenderVersion = $null
if (Test-Path -LiteralPath $BlenderExe -PathType Leaf) {
    $blenderVersion = (& $BlenderExe --version 2>&1 | Select-Object -First 1 | Out-String).Trim()
}
Add-Check -Name "blender_version_read" -Passed (-not [string]::IsNullOrWhiteSpace($blenderVersion)) -Detail $blenderVersion

$lockPath = Resolve-RepoPath $DependencyLock
if (Test-Path -LiteralPath $lockPath -PathType Leaf) {
    $lock = Get-Content -LiteralPath $lockPath -Raw | ConvertFrom-Json
    $allApproved = @($lock.dependencies | Where-Object { -not $_.approved }).Count -eq 0
    $allHashesPresent = @($lock.dependencies | Where-Object { $_.archive -and ([string]::IsNullOrWhiteSpace($_.sha256) -or $_.sha256 -match "REPLACE|PLACEHOLDER") }).Count -eq 0
    Add-Check -Name "dependency_lock_approved" -Passed $allApproved -Detail "status=$($lock.status)"
    Add-Check -Name "dependency_hashes_present" -Passed $allHashesPresent -Detail $lockPath
} else {
    Add-Check -Name "dependency_lock_exists" -Passed $false -Detail $lockPath
}

try {
    $listeners = Get-NetTCPConnection -State Listen -ErrorAction Stop | Where-Object { $_.LocalPort -in $ForbiddenNonLoopbackPorts }
    foreach ($listener in $listeners) {
        $isLoopback = $listener.LocalAddress -in @("127.0.0.1", "::1")
        Add-Check -Name "listener_$($listener.LocalPort)_loopback" -Passed $isLoopback -Detail ("{0}:{1}" -f $listener.LocalAddress, $listener.LocalPort)
    }
} catch {
    Add-Check -Name "listener_inspection" -Passed $false -Detail $_.Exception.Message -Severity "major"
}

$output = Resolve-RepoPath $OutputPath
$outputDir = Split-Path -Parent $output
New-Item -ItemType Directory -Path $outputDir -Force | Out-Null

$blockers = @($checks | Where-Object { -not $_.passed -and $_.severity -eq "blocker" })
$majors = @($checks | Where-Object { -not $_.passed -and $_.severity -eq "major" })
$report = [ordered]@{
    generated_at = (Get-Date).ToString("o")
    repo_root = $RepoRoot
    blender_exe = $BlenderExe
    blender_version = $blenderVersion
    checks = $checks
    blocker_count = $blockers.Count
    major_count = $majors.Count
    production_ready = ($blockers.Count -eq 0 -and $majors.Count -eq 0)
}
$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $output -Encoding UTF8
Write-Host "Environment report written to $output"
Write-Host "Blockers: $($blockers.Count); majors: $($majors.Count); production_ready=$($report.production_ready)"

if ($blockers.Count -gt 0) { exit 2 }
if ($majors.Count -gt 0) { exit 1 }
exit 0

[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)]
    [string]$BlenderExe,

    [string]$PdxZip,
    [string]$PdxSha256,
    [string]$BlenderMcpZip,
    [string]$BlenderMcpSha256,
    [string]$Repository = "user_default",
    [switch]$Apply
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Assert-Executable {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "Blender executable does not exist: $Path"
    }
}

function Assert-ArchiveHash {
    param(
        [string]$Path,
        [string]$ExpectedSha256,
        [string]$Label
    )
    if ([string]::IsNullOrWhiteSpace($Path)) {
        return $false
    }
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        throw "$Label archive does not exist: $Path"
    }
    if ([string]::IsNullOrWhiteSpace($ExpectedSha256) -or $ExpectedSha256 -match "REPLACE|PLACEHOLDER") {
        throw "$Label SHA256 is missing or still a placeholder."
    }
    $actual = (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $ExpectedSha256.ToLowerInvariant()) {
        throw "$Label SHA256 mismatch. Expected $ExpectedSha256 but found $actual"
    }
    Write-Host "$Label checksum verified: $actual"
    return $true
}

function Install-ExtensionArchive {
    param(
        [string]$Path,
        [string]$Label
    )
    $args = @(
        "--command", "extension", "install-file",
        "-r", $Repository,
        "-e", $Path
    )
    Write-Host "Planned $Label command:"
    Write-Host ('"{0}" {1}' -f $BlenderExe, ($args -join ' '))

    if (-not $Apply) {
        Write-Host "Dry run only. Add -Apply after reviewing the version, archive, hash, and profile."
        return
    }

    if ($PSCmdlet.ShouldProcess($Path, "Install $Label into Blender repository $Repository")) {
        & $BlenderExe @args
        if ($LASTEXITCODE -ne 0) {
            throw "$Label installation failed with exit code $LASTEXITCODE. Do not switch to a legacy path silently."
        }
        Write-Host "$Label installation command completed. Run verify_environment.ps1 next."
    }
}

Assert-Executable -Path $BlenderExe
& $BlenderExe --version | Select-Object -First 1

if (Assert-ArchiveHash -Path $PdxZip -ExpectedSha256 $PdxSha256 -Label "io_pdx_mesh") {
    Install-ExtensionArchive -Path (Resolve-Path -LiteralPath $PdxZip).Path -Label "io_pdx_mesh"
}

if (Assert-ArchiveHash -Path $BlenderMcpZip -ExpectedSha256 $BlenderMcpSha256 -Label "Blender Lab MCP") {
    Install-ExtensionArchive -Path (Resolve-Path -LiteralPath $BlenderMcpZip).Path -Label "Blender Lab MCP"
}

if ([string]::IsNullOrWhiteSpace($PdxZip) -and [string]::IsNullOrWhiteSpace($BlenderMcpZip)) {
    Write-Host "No extension archives were supplied. Nothing to install."
}

$ErrorActionPreference = "Stop"

$userScopedMeshyApiKey = [Environment]::GetEnvironmentVariable("MESHY_API_KEY", "User")
if (-not [string]::IsNullOrWhiteSpace($userScopedMeshyApiKey)) {
	$env:MESHY_API_KEY = $userScopedMeshyApiKey
}

if ([string]::IsNullOrWhiteSpace($env:MESHY_API_KEY)) {
	throw "MESHY_API_KEY is missing. Stop before starting Meshy."
}

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..\..\..")).Path
$dependencyLockPath = Join-Path $repoRoot ".tools\3d_pipeline\config\dependencies.lock.json"
$dependencyLock = Get-Content -LiteralPath $dependencyLockPath -Raw | ConvertFrom-Json
$packageVersion = $dependencyLock.routes.meshy_mcp.version
if (-not [string]::IsNullOrWhiteSpace($env:MESHY_MCP_VERSION) -and $env:MESHY_MCP_VERSION -ne $packageVersion) {
	throw "MESHY_MCP_VERSION differs from the dependency lock."
}
$sdkVersion = $dependencyLock.routes.meshy_mcp.resolved_dependencies.modelcontextprotocol_sdk.version
if ([string]::IsNullOrWhiteSpace($sdkVersion)) {
	throw "The dependency lock does not define the Meshy MCP SDK compatibility version."
}
$runtimeVersionSlug = $packageVersion.Replace(".", "_")
$sdkVersionSlug = $sdkVersion.Replace(".", "_")
$runtimeRoot = Join-Path $repoRoot ".tmp\meshy_mcp_native_${runtimeVersionSlug}_sdk_$sdkVersionSlug"
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

$generationToolPath = Join-Path $packageRoot "dist\tools\generation.js"
$compatibilityPatchPath = Join-Path $PSScriptRoot "patch_meshy_mcp.mjs"
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

$compatibilityHashesJson = & $nodeExe $compatibilityPatchPath $packageRoot $repoRoot
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($compatibilityHashesJson)) {
	throw "Failed to apply the locked Meshy MCP artifact compatibility patch."
}
$compatibilityHashes = $compatibilityHashesJson | ConvertFrom-Json
$expectedCompatibilityHashes = $dependencyLock.routes.meshy_mcp.compatibility_file_sha256
if ($null -ne $expectedCompatibilityHashes) {
	foreach ($property in $expectedCompatibilityHashes.PSObject.Properties) {
		$actualHash = $compatibilityHashes.PSObject.Properties[$property.Name].Value
		if ([string]::IsNullOrWhiteSpace($actualHash) -or $actualHash -ne $property.Value.ToLowerInvariant()) {
			throw "Meshy MCP compatibility hash mismatch for $($property.Name)."
		}
	}
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

# Own the exact Node process started by this wrapper. The upstream stdio
# transport does not terminate itself when stdin reaches EOF, so invoking Node
# synchronously leaves both Node and this PowerShell wrapper alive after a
# short-lived MCP client disconnects. A kill-on-close Job Object makes wrapper
# termination tear down only this wrapper's Node tree, while the explicit stdio
# pumps let us detect normal client EOF and close the same owned tree cleanly.
if (-not ([System.Management.Automation.PSTypeName]'ChaosRedux.MeshyProcessJob').Type) {
	Add-Type -TypeDefinition @'
using System;
using System.ComponentModel;
using System.Runtime.InteropServices;

namespace ChaosRedux {
	public static class MeshyProcessJob {
		[StructLayout(LayoutKind.Sequential)]
		private struct JOBOBJECT_BASIC_LIMIT_INFORMATION {
			public long PerProcessUserTimeLimit;
			public long PerJobUserTimeLimit;
			public uint LimitFlags;
			public UIntPtr MinimumWorkingSetSize;
			public UIntPtr MaximumWorkingSetSize;
			public uint ActiveProcessLimit;
			public UIntPtr Affinity;
			public uint PriorityClass;
			public uint SchedulingClass;
		}

		[StructLayout(LayoutKind.Sequential)]
		private struct IO_COUNTERS {
			public ulong ReadOperationCount;
			public ulong WriteOperationCount;
			public ulong OtherOperationCount;
			public ulong ReadTransferCount;
			public ulong WriteTransferCount;
			public ulong OtherTransferCount;
		}

		[StructLayout(LayoutKind.Sequential)]
		private struct JOBOBJECT_EXTENDED_LIMIT_INFORMATION {
			public JOBOBJECT_BASIC_LIMIT_INFORMATION BasicLimitInformation;
			public IO_COUNTERS IoInfo;
			public UIntPtr ProcessMemoryLimit;
			public UIntPtr JobMemoryLimit;
			public UIntPtr PeakProcessMemoryUsed;
			public UIntPtr PeakJobMemoryUsed;
		}

		[DllImport("kernel32.dll", CharSet = CharSet.Unicode, SetLastError = true)]
		private static extern IntPtr CreateJobObject(IntPtr securityAttributes, string name);

		[DllImport("kernel32.dll", SetLastError = true)]
		private static extern bool SetInformationJobObject(
			IntPtr job,
			int informationClass,
			ref JOBOBJECT_EXTENDED_LIMIT_INFORMATION information,
			uint informationLength
		);

		[DllImport("kernel32.dll", SetLastError = true)]
		private static extern bool AssignProcessToJobObject(IntPtr job, IntPtr process);

		[DllImport("kernel32.dll", SetLastError = true)]
		private static extern bool CloseHandle(IntPtr handle);

		public static IntPtr CreateKillOnClose() {
			IntPtr job = CreateJobObject(IntPtr.Zero, null);
			if (job == IntPtr.Zero) {
				throw new Win32Exception(Marshal.GetLastWin32Error(), "Unable to create the Meshy process Job Object.");
			}

			JOBOBJECT_EXTENDED_LIMIT_INFORMATION information = new JOBOBJECT_EXTENDED_LIMIT_INFORMATION();
			information.BasicLimitInformation.LimitFlags = 0x00002000;
			if (!SetInformationJobObject(job, 9, ref information, (uint)Marshal.SizeOf(information))) {
				int error = Marshal.GetLastWin32Error();
				CloseHandle(job);
				throw new Win32Exception(error, "Unable to configure the Meshy process Job Object.");
			}
			return job;
		}

		public static void Assign(IntPtr job, IntPtr process) {
			if (!AssignProcessToJobObject(job, process)) {
				throw new Win32Exception(Marshal.GetLastWin32Error(), "Unable to assign the Meshy Node process to its Job Object.");
			}
		}

		public static void Close(IntPtr job) {
			if (job != IntPtr.Zero) {
				CloseHandle(job);
			}
		}
	}
}
'@
}

$wrapperProcess = Get-CimInstance Win32_Process -Filter "ProcessId = $PID"
$wrapperParentPid = if ($null -eq $wrapperProcess) { 0 } else { [int]$wrapperProcess.ParentProcessId }
$nodeJob = [IntPtr]::Zero
$nodeProcess = $null
$nodeExitCode = 1
$normalClientClosure = $false
try {
	$nodeJob = [ChaosRedux.MeshyProcessJob]::CreateKillOnClose()
	$startInfo = [System.Diagnostics.ProcessStartInfo]::new()
	$startInfo.FileName = $nodeExe
	$startInfo.Arguments = '"' + $entryPoint.Replace('"', '\"') + '"'
	$startInfo.UseShellExecute = $false
	$startInfo.CreateNoWindow = $true
	$startInfo.RedirectStandardInput = $true
	$startInfo.RedirectStandardOutput = $true
	$startInfo.RedirectStandardError = $true
	$startInfo.StandardOutputEncoding = $utf8NoBom
	$startInfo.StandardErrorEncoding = $utf8NoBom

	$nodeProcess = [System.Diagnostics.Process]::new()
	$nodeProcess.StartInfo = $startInfo
	if (-not $nodeProcess.Start()) {
		throw "Failed to start the locked Meshy MCP Node process."
	}
	[ChaosRedux.MeshyProcessJob]::Assign($nodeJob, $nodeProcess.Handle)

	$clientInput = [System.IO.StreamReader]::new([Console]::OpenStandardInput(), $utf8NoBom)
	$clientOutput = [System.IO.StreamWriter]::new([Console]::OpenStandardOutput(), $utf8NoBom)
	$clientError = [System.IO.StreamWriter]::new([Console]::OpenStandardError(), $utf8NoBom)
	$clientOutput.AutoFlush = $true
	$clientError.AutoFlush = $true
	$nodeInput = [System.IO.StreamWriter]::new($nodeProcess.StandardInput.BaseStream, $utf8NoBom)
	$nodeInput.AutoFlush = $true
	$pendingIds = [System.Collections.Generic.HashSet[string]]::new()
	$responseIds = [System.Collections.Generic.HashSet[string]]::new()
	$inputClosed = $false
	$outputClosed = $false
	$errorClosed = $false
	$inputRead = $clientInput.ReadLineAsync()
	$outputRead = $nodeProcess.StandardOutput.ReadLineAsync()
	$errorRead = $nodeProcess.StandardError.ReadLineAsync()

	while ($true) {
		if (-not $inputClosed -and $inputRead.IsCompleted) {
			$inputLine = $inputRead.GetAwaiter().GetResult()
			if ($null -eq $inputLine) {
				$inputClosed = $true
				$normalClientClosure = $true
				$nodeInput.Close()
			}
			else {
				$nodeInput.WriteLine($inputLine)
				try {
					$message = $inputLine | ConvertFrom-Json -ErrorAction Stop
					$idProperty = $message.PSObject.Properties['id']
					if ($null -ne $idProperty) {
						$idToken = $idProperty.Value | ConvertTo-Json -Compress
						$null = $pendingIds.Add($idToken)
					}
				}
				catch [System.ArgumentException] {
				}
				$inputRead = $clientInput.ReadLineAsync()
			}
		}

		if (-not $outputClosed -and $outputRead.IsCompleted) {
			$outputLine = $outputRead.GetAwaiter().GetResult()
			if ($null -eq $outputLine) {
				$outputClosed = $true
			}
			else {
				$clientOutput.WriteLine($outputLine)
				try {
					$message = $outputLine | ConvertFrom-Json -ErrorAction Stop
					$idProperty = $message.PSObject.Properties['id']
					if ($null -ne $idProperty) {
						$idToken = $idProperty.Value | ConvertTo-Json -Compress
						$null = $responseIds.Add($idToken)
					}
				}
				catch [System.ArgumentException] {
				}
				$outputRead = $nodeProcess.StandardOutput.ReadLineAsync()
			}
		}

		if (-not $errorClosed -and $errorRead.IsCompleted) {
			$errorLine = $errorRead.GetAwaiter().GetResult()
			if ($null -eq $errorLine) {
				$errorClosed = $true
			}
			else {
				$clientError.WriteLine($errorLine)
				$errorRead = $nodeProcess.StandardError.ReadLineAsync()
			}
		}

		if ($wrapperParentPid -gt 0 -and -not (Get-Process -Id $wrapperParentPid -ErrorAction SilentlyContinue)) {
			break
		}

		# The pinned SDK does not exit on stdin EOF. Once every request accepted
		# before EOF has produced its matching response, the wrapper can close its
		# exact Node job without truncating a long-running provider operation.
		$allResponsesReceived = $true
		foreach ($pendingId in $pendingIds) {
			if (-not $responseIds.Contains($pendingId)) {
				$allResponsesReceived = $false
				break
			}
		}
		if ($inputClosed -and $allResponsesReceived) {
			break
		}
		if ($nodeProcess.HasExited -and $outputClosed -and $errorClosed) {
			break
		}
		Start-Sleep -Milliseconds 10
	}

	if ($nodeProcess.HasExited) {
		$nodeExitCode = $nodeProcess.ExitCode
	}
	elseif ($normalClientClosure) {
		$nodeExitCode = 0
	}
}
finally {
	if ($nodeJob -ne [IntPtr]::Zero) {
		[ChaosRedux.MeshyProcessJob]::Close($nodeJob)
		$nodeJob = [IntPtr]::Zero
	}
	if ($null -ne $nodeProcess) {
		if (-not $nodeProcess.HasExited) {
			try {
				$nodeProcess.Kill()
			}
			catch [System.InvalidOperationException] {
			}
		}
		try {
			$nodeProcess.WaitForExit(5000) | Out-Null
		}
		catch [System.SystemException] {
		}
		$nodeProcess.Dispose()
	}
}

exit $nodeExitCode

param([Parameter(Mandatory=$true)][int]$GameProcessId, [Parameter(Mandatory=$true)][string]$OutputPath)
$gameProcess = Get-Process -Id $GameProcessId -ErrorAction Stop
if ($gameProcess.ProcessName -ne 'hoi4') { throw 'The recorded process is not HOI4.' }
$windowHandle = $gameProcess.MainWindowHandle
if ($windowHandle -eq [IntPtr]::Zero) { throw 'HOI4 has no main window yet.' }
Add-Type -AssemblyName System.Drawing
Add-Type @'
using System;
using System.Runtime.InteropServices;
public class Hoi4WindowCapture {
    [StructLayout(LayoutKind.Sequential)] public struct Rect { public int Left, Top, Right, Bottom; }
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr window, out Rect rect);
    [DllImport("user32.dll")] public static extern bool PrintWindow(IntPtr window, IntPtr context, uint flags);
}
'@
$bounds = New-Object Hoi4WindowCapture+Rect
if (-not [Hoi4WindowCapture]::GetWindowRect($windowHandle, [ref]$bounds)) { throw 'Could not read HOI4 window bounds.' }
$width = $bounds.Right - $bounds.Left
$height = $bounds.Bottom - $bounds.Top
if ($width -le 0 -or $height -le 0) { throw 'HOI4 has invalid window bounds.' }
$bitmap = New-Object System.Drawing.Bitmap($width, $height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$context = $graphics.GetHdc()
try { $captured = [Hoi4WindowCapture]::PrintWindow($windowHandle, $context, 2) }
finally { $graphics.ReleaseHdc($context) }
try {
    if (-not $captured) { throw 'HOI4 did not provide a window capture.' }
    $bitmap.Save($OutputPath, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Output $OutputPath
} finally { $graphics.Dispose(); $bitmap.Dispose() }

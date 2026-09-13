# Setup and launch evidence

No in-game console commands were used.
No test-country setup, campaign state, or save was created.

The existing shortcut `C:/Users/klimp/OneDrive/Desktop/hoi4.exe - Shortcut.lnk` was inspected through `WScript.Shell` before launch.
Its verified target is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/hoi4.exe`, its arguments are `-debug`, and its working directory is the installed game directory.
Launch uses `Start-Process -FilePath <verified shortcut> -WindowStyle Hidden`.
The initial and final process state, launch time, and process ID are recorded per cycle.

Window capture uses `capture_hoi4_window.ps1` with that recorded PID.
The helper verifies the process name, obtains only the HOI4 window bounds, and captures that window using `PrintWindow`.
The resulting image is reviewed directly before main-menu acceptance is recorded.

Before a repair relaunch, the parent verifies the recorded process is still named `hoi4`, requests `CloseMainWindow()`, waits five seconds, and stops only that PID if it remains running.
The final accepted process may remain open at the menu.

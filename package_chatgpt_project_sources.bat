@echo off
where py >nul 2>nul
if errorlevel 1 (
	echo Python 3 was not found. Install Python and enable the Windows Python launcher.
	pause
	exit /b 1
)
py -3 "%~dp0.tools\package_chatgpt_project_sources.py" --pause %*
exit /b %errorlevel%

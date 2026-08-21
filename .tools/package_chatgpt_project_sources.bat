@echo off
setlocal
title Chaos Redux source packager
cd /d "%~dp0"

echo Packaging Chaos Redux project sources...
echo.

where py >nul 2>nul
if errorlevel 1 (
	echo ERROR: Python 3 was not found.
	echo Install Python and enable the Windows Python launcher, then try again.
	echo.
	pause
	exit /b 1
)

py -3 "%~dp0package_chatgpt_project_sources.py" --open %*
set "package_exit_code=%errorlevel%"

echo.
if not "%package_exit_code%"=="0" (
	echo Packaging failed. The error is shown above.
) else (
	echo Packaging finished. The output folder has been opened.
)
echo.
pause
exit /b %package_exit_code%

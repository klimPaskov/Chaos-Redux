@echo off
setlocal

powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_meshy_mcp.ps1"
exit /b %errorlevel%

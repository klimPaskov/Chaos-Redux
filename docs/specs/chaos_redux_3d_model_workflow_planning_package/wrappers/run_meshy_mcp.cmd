@echo off
setlocal

if "%MESHY_API_KEY%"=="" (
  echo ERROR: MESHY_API_KEY is not set. The key must be supplied through the user environment or a secret manager. 1>&2
  exit /b 2
)

if "%MESHY_MCP_VERSION%"=="" set "MESHY_MCP_VERSION=0.4.0"
set "TRANSPORT=stdio"

where npx >nul 2>nul
if errorlevel 1 (
  echo ERROR: npx was not found on PATH. 1>&2
  exit /b 3
)

call npx -y @meshy-ai/meshy-mcp-server@%MESHY_MCP_VERSION%
set "exit_code=%ERRORLEVEL%"
endlocal & exit /b %exit_code%

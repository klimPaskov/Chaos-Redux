@echo off
setlocal

if "%MESHY_API_KEY:~0,1%"=="" goto missing_meshy_key

set "PIPELINE_ROOT=%~dp0.."
set "BLENDER_MCP_PROJECT=%PIPELINE_ROOT%\vendor\blender_mcp\mcp"
if "%UV_EXE%"=="" set "UV_EXE=C:\Program Files\Python313\Scripts\uv.exe"
if not exist "%UV_EXE%" (
    for /f "delims=" %%U in ('where uv.exe 2^>nul') do if not defined UV_EXE set "UV_EXE=%%U"
)
if not exist "%UV_EXE%" (
    echo uv.exe is required for the locked Blender Lab MCP route.
    exit /b 3
)
if not exist "%BLENDER_MCP_PROJECT%\pyproject.toml" (
    echo Locked Blender Lab MCP project is missing: %BLENDER_MCP_PROJECT%
    exit /b 4
)

"%UV_EXE%" --directory "%BLENDER_MCP_PROJECT%" run blender-mcp
exit /b %errorlevel%

:missing_meshy_key
echo MESHY_API_KEY is missing. Stop before starting the workflow.
exit /b 2

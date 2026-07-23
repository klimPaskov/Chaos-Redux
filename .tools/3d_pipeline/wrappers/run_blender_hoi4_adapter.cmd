@echo off
setlocal

if "%MESHY_API_KEY:~0,1%"=="" goto missing_meshy_key

set "PIPELINE_ROOT=%~dp0.."
set "REPO_ROOT=%PIPELINE_ROOT%\..\.."
set "ADAPTER_ROOT=%PIPELINE_ROOT%\adapter"
set "CHAOS_REDUX_MOD_ROOT=%REPO_ROOT%"
set "CHAOS_REDUX_3D_JOB_ROOT=%REPO_ROOT%\docs\assets\chaos_redux_3d_model_pilots\models_3d"
set "CHAOS_REDUX_3D_CONFIG=%PIPELINE_ROOT%\config\blender_hoi4_adapter.json"
if "%UV_EXE%"=="" set "UV_EXE=C:\Program Files\Python313\Scripts\uv.exe"
if not exist "%UV_EXE%" (
    for /f "delims=" %%U in ('where uv.exe 2^>nul') do if not defined UV_EXE set "UV_EXE=%%U"
)
if not exist "%UV_EXE%" (
    echo uv.exe is required for the locked Blender HOI4 adapter.
    exit /b 3
)
if not exist "%ADAPTER_ROOT%\pyproject.toml" (
    echo Blender HOI4 adapter project is missing: %ADAPTER_ROOT%
    exit /b 4
)

"%UV_EXE%" --directory "%ADAPTER_ROOT%" run python -m chaosx_blender_hoi4_mcp %*
exit /b %errorlevel%

:missing_meshy_key
echo MESHY_API_KEY is missing. Stop before starting the workflow.
exit /b 2

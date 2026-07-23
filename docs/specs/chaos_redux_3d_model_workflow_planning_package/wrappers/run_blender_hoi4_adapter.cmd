@echo off
setlocal

if "%CHAOS_REDUX_MOD_ROOT%"=="" (
  echo ERROR: CHAOS_REDUX_MOD_ROOT is not set. 1>&2
  exit /b 2
)

if "%CHAOS_REDUX_3D_JOB_ROOT%"=="" (
  echo ERROR: CHAOS_REDUX_3D_JOB_ROOT is not set. 1>&2
  exit /b 2
)

where python >nul 2>nul
if errorlevel 1 (
  echo ERROR: python was not found on PATH. 1>&2
  exit /b 3
)

python -m chaosx_blender_hoi4_mcp %*
set "exit_code=%ERRORLEVEL%"
endlocal & exit /b %exit_code%

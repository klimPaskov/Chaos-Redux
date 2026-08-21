@echo off
call "%~dp0.tools\package_chatgpt_project_sources.bat" %*
exit /b %errorlevel%

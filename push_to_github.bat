@echo off
cd /d "%~dp0"
echo ===================================================
echo Pushing Olympics Project to GitHub...
echo Repository: https://github.com/Anuj160904/Olympics.git
echo ===================================================
"..\MinGit\cmd\git.exe" push -u origin main --force
echo.
if %ERRORLEVEL% equ 0 (
    echo [SUCCESS] Project successfully pushed to GitHub!
) else (
    echo [NOTE] Sign in as Anuj160904 or invite Pari031207 as collaborator.
)
pause

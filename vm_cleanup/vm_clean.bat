@echo off
set ORIGDIR="%CD%"
set SCRIPTDIR=%~dp0

set CLEANEREXE="C:\Program Files (x86)\Glary Utilities 5\DiskCleaner.exe"

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    

echo.
echo Fixing msinfo32/dxdiag conflict...
reg import "%SCRIPTDIR%\msinfo_fix.reg"
if errorlevel 1 goto ERROR
echo Fixed msinfo32/dxdiag conflict

echo.
echo Clearing explorer search history...
reg import "%SCRIPTDIR%\delete_search.reg"
if errorlevel 1 goto ERROR
echo Cleared explorer search history.

echo.
echo Clearing run history...
reg import "%SCRIPTDIR%\delete_runs.reg"
if errorlevel 1 goto ERROR
echo Run history deleted.

echo.
echo Running disk cleaner, this script will continue when it's closed...
%CLEANEREXE%
rem if errorlevel 1 goto ERROR
echo Disk cleaner closed.

echo.
echo Defragging...
defrag C: /U
if errorlevel 1 goto ERROR
echo Defrag done.

echo.
echo Zeroing free space...
sdelete C: /z
if errorlevel 1 goto ERROR
echo Free space has been zeroed.
goto END


:ERROR
echo An error occured, see above.
pause
goto HARDEND

END:
echo Shutting down...
timeout 3
call shutdown /p /f

:HARDEND

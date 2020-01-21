@echo off
set ORIGDIR="%CD%"
set SCRIPTDIR="%~dp0"

cd "%SCRIPTDIR%"

echo Building portable EXE...
call conda run -n scambait_popup_gen pyinstaller ^
    --noconfirm ^
    --add-data scambait_megalist.txt;. ^
    --onefile ^
    --icon=scambait_popup_gen.ico ^
    scambait_popup_gen.py

cd "%ORIGDIR%"
pause
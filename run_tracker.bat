@echo off
cd /d "G:\PROGRAMMING\MAJOR PROJECTS\TPO-tracker"

mkdir logs 2>nul

set "LOG_FILE=logs\log.txt"

echo ==================================================>> "%LOG_FILE%"
echo [%date% %time%] Task started>> "%LOG_FILE%"

.\.venv\Scripts\python.exe -u main.py >> "%LOG_FILE%" 2>&1
set "EXIT_CODE=%ERRORLEVEL%"

echo [%date% %time%] Task finished with exit code %EXIT_CODE%>> "%LOG_FILE%"
exit /b %EXIT_CODE%
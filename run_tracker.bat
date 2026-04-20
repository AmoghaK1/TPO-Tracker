@echo off
cd /d "G:\PROGRAMMING\MAJOR PROJECTS\TPO-tracker"

mkdir logs 2>nul

.\.venv\Scripts\python.exe main.py >> logs\log.txt 2>&1
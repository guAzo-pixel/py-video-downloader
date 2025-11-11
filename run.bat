@echo off
ECHO ==========================================================
ECHO py-video-downloader Launcher
ECHO ==========================================================
ECHO.

REM 1. Check if Python is in PATH
where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] Python not found.
    ECHO Please install Python and ensure "Add Python to PATH" was checked.
    ECHO.
    PAUSE
    EXIT /B 1
)

REM 2. Check for venv and create if it doesn't exist
IF NOT EXIST venv (
    ECHO [INFO] Creating virtual environment (first-time setup)
    python -m venv venv
    IF %ERRORLEVEL% NEQ 0 (
        ECHO [ERROR] Failed to create venv. Check Python installation.
        PAUSE
        EXIT /B 1
    )
    ECHO [INFO] Virtual environment 'venv' created.
)

REM 3. Activate environment and install requirements
ECHO [INFO] Activating environment and installing requirements
CALL venv\Scripts\activate.bat

REM Instalar requisitos (el "> nul 2>&1" suprime la salida, para limpieza)
pip install -r requirements.txt > nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO [ERROR] Failed to install requirements from requirements.txt.
    ECHO Check the file contents and internet connection.
    PAUSE
    EXIT /B 1
)

ECHO [INFO] Requirements ready. Starting application
ECHO ==========================================================
ECHO.

REM 4. Run the main script (Asegúrate de que tu script se llame 'main.py')
python main.py

ECHO.
ECHO ==========================================================
ECHO Program finished. Press any key to exit.
PAUSE
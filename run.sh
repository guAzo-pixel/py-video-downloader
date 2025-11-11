#!/bin/bash

echo "=========================================================="
echo " py-video-downloader Launcher"
echo "=========================================================="
echo ""

if ! command -v python3 &> /dev/null
then
    echo "[ERROR] python3 could not be found."
    echo "Please install python3 to continue."
    exit 1
fi

if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment (first-time setup)..."
    python3 -m venv venv
    echo "[INFO] Virtual environment 'venv' created."
fi

echo "[INFO] Activating virtual environment..."
source venv/bin/activate

pip show yt-dlp > /dev/null 2>&1

if [ $? -ne 0 ]; then
  echo "[INFO] 'yt-dlp' not found. Installing requirements..."
  pip install -r requirements.txt > /dev/null 2>&1
  echo "[INFO] Requirements installed."
else
  echo "[INFO] Requirements already satisfied."
fi

echo "[INFO] Starting application..."
echo "=========================================================="
echo ""

python3 main.py

echo ""
echo "=========================================================="
echo "Program finished. Press Enter to exit."
read
# py-video-downloader

A simple command-line utility for downloading YouTube videos or audio locally, relying only on Python and `yt_dlp`.

## Features

* **Video or Audio:** Choose to download the full video (MP4, max 720p) or audio-only (best available quality).
* **Simple Interface:** A straightforward interactive prompt for a URL and format choice.
* **Organized:** All downloads are saved to a dedicated `material_archivado_youtube` directory.

## Requirements

* Python 3.x
* `yt_dlp`

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/](https://github.com/)[YOUR_USERNAME]/py-video-downloader.git
    cd py-video-downloader
    ```

2.  (Recommended) Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script from your terminal:

```bash
python main.py
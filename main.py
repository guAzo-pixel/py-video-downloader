import os
import yt_dlp
from typing import Optional

DOWNLOAD_PATH = "youtube_archive_material"

def get_user_choice(prompt: str, choices: list) -> str:
    while True:
        user_input = input(f"{prompt} ({'/'.join(choices)}): ").strip().lower()
        if user_input in choices:
            return user_input
        print(f"Invalid option. Please enter one of the following: {', '.join(choices)}")

def download_youtube_material_pure_python():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Audio will be downloaded in M4A/WebM format (high quality), not MP3.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    url = input("Enter the YouTube video URL: ").strip()
    if not url:
        print("No URL entered. Exiting program.")
        return

    choice = get_user_choice("Do you want [v]ideo or [a]udio only?", ['v', 'a'])
    
    output_template = os.path.join(DOWNLOAD_PATH, '%(title)s.%(ext)s')
    
    ydl_opts = {
        'format': '',
        'outtmpl': output_template,
        'cachedir': False,
        'noplaylist': True,
        'logtostderr': True,
        'noprogress': False,
        'postprocessors': [], 
    }

    if choice == 'a':
        ydl_opts['format'] = 'bestaudio' 
        print("\nPreparing download: Audio Only (M4A or WebM - Max quality)...")
    else: 
        ydl_opts['format'] = 'best[ext=mp4][height<=720]/best'
        print("\nPreparing download: Video and Audio (MP4/WebM - Max 720p Progressive)...")
        
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)
        print(f"Created save directory: {DOWNLOAD_PATH}")
        
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Video')
            print(f"\n✅ Video loaded: **{title}**")
            print(f"⬇️ Downloading '{title}'...")
            
            ydl.download([url])

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Task finished.")
        
    except yt_dlp.utils.DownloadError as e:
        print(f"\n yt-dlp Download Error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    download_youtube_material_pure_python()
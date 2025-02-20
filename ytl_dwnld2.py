import yt_dlp
import os

def download_youtube_playlist(url, resolution="1080p", download_path="./"):
    try:
        # Ensure the download path exists
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # Define the download options
        ydl_opts = {
            'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best[height<={resolution[:-1]}]',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_path, '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'noplaylist': False,  # Ensure we do not ignore the playlist
            'yesplaylist': True   # Confirm we want to download the playlist
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the playlist
            ydl.download([url])
        
        print(f"Downloaded playlist successfully to {download_path}!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# URL of the YouTube playlist to be downloaded
playlist_url = "https://youtube.com/playlist?list=PLZTiWdqxlvACZJEFL0XMslGoBCfz3wgSl&si=BzVkrH_Z-RqImYpo"

# Path where the playlist should be downloaded
download_path = "./downloads"

# Call the function to download the playlist
download_youtube_playlist(playlist_url, download_path=download_path)

# YouTube Video Downloader

A Python script to download YouTube videos using the `pytube` library. You can specify the YouTube video URL as a command-line argument.

## How to Use

1. Clone the repository.
2. Install the required dependencies: `pip install pytube`.
3. Run the script with the desired YouTube video URL and an optional output directory.

   ```bash
   python youtube_video_download.py "https://www.youtube.com/watch?v=VIDEO_ID" --output downloaded_videos
    ```
- Replace "https://www.youtube.com/watch?v=VIDEO_ID" with the actual YouTube video URL you want to download.
- Replace "downloaded_videos" with the desired output directory. If you don't specify an output directory, the script will use the default directory "downloaded_videos".

import argparse
from pytube import YouTube

def download_video(video_url, output_path):
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path=output_path)
    print(f"Video '{yt.title}' has been downloaded successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("--output", default="downloaded_videos", help="Output directory")

    args = parser.parse_args()
    download_video(args.url, args.output)

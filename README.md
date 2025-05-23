# YouTube Downloader

A simple command-line tool to download YouTube videos as MP4 or extract audio as MP3.

## Overview

This Python application allows you to download videos from YouTube in either video (MP4) or audio (MP3) format. It features:

- Clean URL processing (removes tracking parameters)
- Progress bar visualization during downloads
- Support for both video and audio extraction
- Simple command-line interface

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/SiFuMax09/youtubedownloader.git
   cd youtubedownloader
   ```

2. Install the required dependencies:
   ```
   pip install pytubefix
   ```

## Usage

Run the script using Python:

```
python main.py
```

Follow the prompts:
1. Enter a YouTube URL when asked
2. Choose your desired format (mp4 or mp3)
3. Wait for the download to complete

Example:
```
🔗 YouTube-URL eingeben: https://www.youtube.com/watch?v=dQw4w9WgXcQ
🎞️ Format wählen (mp4 oder mp3): mp4

🔧 Ursprüngliche URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
✅ Bereinigte URL:   https://www.youtube.com/watch?v=dQw4w9WgXcQ
🎬 Titel: Rick Astley - Never Gonna Give You Up (Official Music Video)
⬇️ Starte Download von: https://www.youtube.com/watch?v=dQw4w9WgXcQ
📥 [==================================================] 100.0%
✅ Erfolgreich als MP4 gespeichert: /path/to/Rick Astley - Never Gonna Give You Up (Official Music Video).mp4
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is for personal use only. Please respect YouTube's terms of service and copyright laws when downloading content.


from pytubefix import YouTube
import os
import re
import sys

def clean_url(url):
    """
    Entfernt alle Parameter aus YouTube-URLs wie ?si=... oder &t=...
    """
    original_url = url
    if "youtu.be/" in url:
        match = re.match(r"(https?://youtu\.be/[\w\-]+)", url)
        cleaned = match.group(1) if match else url
    elif "youtube.com/watch" in url:
        match = re.match(r"(https?://www\.youtube\.com/watch\?v=[\w\-]+)", url)
        cleaned = match.group(1) if match else url
    else:
        cleaned = url

    print(f"\n🔧 Ursprüngliche URL: {original_url}")
    print(f"✅ Bereinigte URL:   {cleaned}")
    return cleaned

def show_progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_bar_length = 50  # Länge der Anzeige

    done = int(progress_bar_length * bytes_downloaded / total_size)
    sys.stdout.write(f"\r📥 [{('=' * done)}{' ' * (progress_bar_length - done)}] {percentage_of_completion:5.1f}%")
    sys.stdout.flush()

def download_youtube_video(url, format_choice):
    try:
        cleaned_url = clean_url(url)
        yt = YouTube(cleaned_url, on_progress_callback=show_progress_bar, use_po_token=True)
        yt.po_token = "MnSVQKnuH-YmzJV4AUuLiTcRcCgmYuNaY6v_OTqXXe2tktPU9BQrMZLAS511pF4j5LykfHQnYDoAAez-qcu9BtBUI0DiEfgkCRXT3ivtSgEHfEJiRWF4XC7phWdLgZOPq4yQHHE5Ig7WW_NuQnYlRrKe6XsX7Q=="


        print(f"\n🎬 Titel: {yt.title}")

        if format_choice.lower() == "mp4":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        elif format_choice.lower() == "mp3":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            print("❌ Ungültiges Format gewählt. Nur 'mp4' oder 'mp3' erlaubt.")
            return

        print(f"⬇️ Starte Download von: {cleaned_url}")
        out_file = stream.download()

        if format_choice.lower() == "mp3":
            base, _ = os.path.splitext(out_file)
            new_file = base + ".mp3"
            os.rename(out_file, new_file)
            print(f"\n✅ Erfolgreich als MP3 gespeichert: {new_file}")
        else:
            print(f"\n✅ Erfolgreich als MP4 gespeichert: {out_file}")

    except Exception as e:
        print(f"\n❌ Fehler beim Download von:\n   {url}")
        print(f"🔍 Fehlermeldung: {e}")

if __name__ == "__main__":
    video_url = input("🔗 YouTube-URL eingeben: ").strip()
    format_choice = input("🎞️ Format wählen (mp4 oder mp3): ").strip()

    if video_url:
        download_youtube_video(video_url, format_choice)
    else:
        print("❌ Keine gültige URL eingegeben.")

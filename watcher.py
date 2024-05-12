import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from playlist import save_playlist

DEFAULT_PLAYLIST = r"C:\Users\PATRIX\AppData\Roaming\PotPlayerMini64\Playlist"


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        save_playlist()


def monitor_file(file_path):
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=file_path, recursive=True)
    observer.start()
    print("Watching...")
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()


if __name__ == "__main__":
    monitor_file(DEFAULT_PLAYLIST)

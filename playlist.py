import subprocess
import potplayer
import os

DEFAULT_PLAYLIST = (
    r"C:\Users\PATRIX\AppData\Roaming\PotPlayerMini64\Playlist\PotPlayerMini64.dpl"
)
PROGRAM_PATH = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
STORAGE_PATH = (
    "C:\\Users\\PATRIX\\Documents\\Code\\Python\\potplayer-playlist\\playlists\\"
)


def pick_playlist():
    print("Current Pot Player Playlists:")
    playlists = os.listdir(STORAGE_PATH)
    for k, v in enumerate(playlists):
        print(k, v)

    if len(playlists) > 1:
        selected_ind = int(input("Enter the index of a playlist: "))
        return playlists[selected_ind]
    elif len(playlists) == 1:
        return playlists[0]
    else:
        return None


def start_program(program_path):
    return subprocess.Popen(program_path)


def change_playlist(path):
    abspath = "{0}{1}".format(STORAGE_PATH, path)
    with open(abspath, "r") as f:
        playlist = potplayer.PlayList.load(abspath)
        playlist.dump(DEFAULT_PLAYLIST)


def monitor_and_execute(process):
    process.wait()  # Wait for the process to terminate
    print("Process has terminated.")


def save_playlist():
    with open(DEFAULT_PLAYLIST, "r") as f:
        playlist = potplayer.PlayList.load(DEFAULT_PLAYLIST)
        parent_folder = os.path.dirname(playlist.file_list[0])
        parent_folder = parent_folder.split("\\")[-1]
        playlist.header = parent_folder
        playlist.dump("{0}{1}".format(STORAGE_PATH, parent_folder))

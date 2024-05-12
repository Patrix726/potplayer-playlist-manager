import subprocess
import potplayer
import os
import curses

DEFAULT_PLAYLIST = (
    r"C:\Users\PATRIX\AppData\Roaming\PotPlayerMini64\Playlist\PotPlayerMini64.dpl"
)
PROGRAM_PATH = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
STORAGE_PATH = (
    "C:\\Users\\PATRIX\\Documents\\Code\\Python\\potplayer-playlist\\playlists\\"
)


def pick_playlist(stdscr):
    playlists = os.listdir(STORAGE_PATH)
    if len(playlists) == 0:
        return None
    elif len(playlists) == 1:
        return playlists[0]
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()  # Clear the screen
    stdscr.addstr("Current Pot Player Playlists:")
    # print("Current Pot Player Playlists:")
    selected_ind = 0
    while True:
        for index, option in enumerate(playlists):
            if index == selected_ind:
                stdscr.addstr(index + 1, 0, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(index + 1, 0, f"  {option}")

        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == curses.KEY_DOWN:
            selected_ind = min(selected_ind + 1, len(playlists) - 1)
        elif key == curses.KEY_UP:
            selected_ind = max(selected_ind - 1, 0)
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Handle Enter key
            break

    # Print the selected option
    stdscr.clear()
    return playlists[selected_ind]


def start_program(program_path):
    return subprocess.Popen([program_path])


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

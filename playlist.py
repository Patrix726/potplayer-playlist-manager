import subprocess
import potplayer
import os
import curses

USERNAME = os.environ["USERNAME"]
DEFAULT_PLAYLIST = f"C:\\Users\\{USERNAME}\\AppData\\Roaming\\PotPlayerMini64\\Playlist\\PotPlayerMini64.dpl"
PROGRAM_PATH = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
WORKING_DIR = os.path.dirname(__file__)
STORAGE_PATH = os.path.join(WORKING_DIR, "playlists")


def pick_playlist(stdscr):
    playlists = os.listdir(STORAGE_PATH)
    if len(playlists) == 0:
        return None
    elif len(playlists) == 1:
        return playlists[0]  # return the only playlist

    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()  # Clear the screen

    selected_ind = 0
    while True:
        stdscr.addstr("Current Pot Player Playlists:")  # Title

        for index, playlist in enumerate(playlists):
            playlist = playlist.rstrip(".dpl")  # remove the extension
            if index == selected_ind:
                stdscr.addstr(index + 1, 0, f"> {playlist}", curses.A_REVERSE)
            else:
                stdscr.addstr(index + 1, 0, f"  {playlist}")

        stdscr.refresh()
        # Get user input
        key = stdscr.getch()

        # Handle user input
        if key == curses.KEY_DOWN:  # Handle Down Key
            selected_ind = min(selected_ind + 1, len(playlists) - 1)
        elif key == curses.KEY_UP:  # Handle Up Key
            selected_ind = max(selected_ind - 1, 0)
        elif key == curses.KEY_DC:  # Handle Delete key
            os.remove(os.path.join(STORAGE_PATH, playlists[selected_ind]))
            playlists.pop(selected_ind)
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Handle Enter key
            break
        stdscr.clear()

    stdscr.clear()

    # return the selected playlist
    return playlists[selected_ind]


def start_program(program_path):
    return subprocess.Popen([program_path])


def change_playlist(path):
    abspath = "{0}{1}".format(STORAGE_PATH, path)

    # Load the selected playlist path
    playlist = potplayer.PlayList.load(abspath)

    # Dump the loaded playlist at the default playlist path
    playlist.dump(DEFAULT_PLAYLIST)


def save_playlist():
    # Load the default playlist
    playlist = potplayer.PlayList.load(DEFAULT_PLAYLIST)

    # find out the path of the files inside the playlist
    parent_folder = os.path.dirname(playlist.file_list[0])

    # exception.txt file  path
    exception_file = "".join([WORKING_DIR, "exceptions.txt"])

    with open(exception_file, "r") as f:
        for path in f.readlines():
            try:
                # find the common path between the exception path and the playlist
                common_path = os.path.commonpath([os.path.abspath(path), parent_folder])

                # if the common path is the same as the exception path don't save the playlistS
                if common_path == path:
                    return
            except:
                continue

    # join the two parent directories for optimum naming
    parent_folder = ".".join(parent_folder.split("\\")[-2:])

    playlist.header = parent_folder
    # save the playlist inside the storage path
    playlist.dump("{0}{1}".format(STORAGE_PATH, parent_folder))

import curses
import time
import potplayer
from playlist import (
    pick_playlist,
    change_playlist,
    start_program,
    monitor_and_execute,
    save_playlist,
    PROGRAM_PATH,
    DEFAULT_PLAYLIST,
)


if __name__ == "__main__":
    # program_path = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
    picked_playlist = curses.wrapper(pick_playlist)
    if picked_playlist != None:
        change_playlist(picked_playlist)

    process = start_program(PROGRAM_PATH)
    time.sleep(10)
    # potplayer.run(DEFAULT_PLAYLIST)
    # monitor_and_execute(process)

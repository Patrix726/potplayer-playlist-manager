import curses
from playlist import (
    pick_playlist,
    change_playlist,
    start_program,
    PROGRAM_PATH,
)


if __name__ == "__main__":
    # Call the pick playlist function
    picked_playlist = curses.wrapper(pick_playlist)

    if picked_playlist != None:
        change_playlist(picked_playlist)
        process = start_program(PROGRAM_PATH)
    else:
        print("You have no saved playlists")

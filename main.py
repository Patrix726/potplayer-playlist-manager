from playlist import (
    pick_playlist,
    change_playlist,
    start_program,
    monitor_and_execute,
    save_playlist,
    PROGRAM_PATH,
)


if __name__ == "__main__":
    # program_path = r"C:\Program Files\DAUM\PotPlayer\PotPlayerMini64.exe"
    picked_playlist = pick_playlist()
    if picked_playlist != None:
        change_playlist(picked_playlist)

    process = start_program(PROGRAM_PATH)
    monitor_and_execute(process, save_playlist)

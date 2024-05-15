# PotPlayer Playlist Manager

PotPlayer Playlist Manager is a handy tool designed to enhance your experience with PotPlayer, a popular media player on Windows. This project aims to simplify playlist management by providing features like playlist backup, folder exceptions, and an interactive command-line interface (CLI) for effortless usage.

## Features

### Playlist Backup
Easily backup opened playlists along with their track time. Never worry about losing your playlists again!

### Folder Exception
Customize your playlist management by specifying exception folders. Choose which folders to exclude from your playlist management for a personalized experience.

### Interactive CLI
Enjoy a user-friendly CLI interface that makes navigating and managing playlists a breeze. No need to deal with complex commands or confusing interfaces.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository to your local machine.
    ```
    git clone https://github.com/Patrix726/potplayer-playlist-manager.git
    ```
2. Navigate to the project directory.
    ```
    cd potplayer-playlist-manager
    ```
3. Install dependencies.
    ```
    pip install -r requirements.txt
    ```

### Usage

1. **PotPlayer Playlist Manager CLI:**

   - **potPlaylist.bat:** Use this batch file to open the command-line interface (CLI) tool for managing backed up playlists. This tool allows you to select and open playlists that have been previously backed up, as well as delete backed up playlists if needed. Simply double-click on `potPlaylist.bat` to launch the CLI tool.

   - **Select Playlist:** Upon launching `potPlaylist.bat`, you will be presented with a list of playlists that have been previously backed up. Use the arrow keys to navigate through the list and press Enter to select a playlist to open in PotPlayer.

   - **Delete Playlist:** If you wish to delete a backed up playlist, navigate to the playlist in the CLI tool and press the appropriate key ("Delete").

   - **Note:** This CLI tool only works with playlists that have been previously backed up using the PotPlayer Playlist Manager. If you need to manage other playlists, consider backing them up using the PotPlayer Playlist Manager first.

2. **PotPlayer Playlist Watcher:**

   - **potWatcher.bat:** Run this batch file to watch for changes in the default playlist opened by PotPlayer. Additionally, this script automatically backs up playlists opened by PotPlayer and stores them inside the `playlists` folder, ensuring that your playlists are always safe and accessible. Note that this script requires a command prompt window to work, as it displays real-time changes detected in the playlist.

   - **hidePotWatcher.vbs:** Alternatively, you can run the `hidePotWatcher.vbs` script to run the PotPlayer Playlist Watcher in the background without displaying a command prompt window. This is useful if you prefer a non-intrusive way of monitoring playlist changes. To use `hidePotWatcher.vbs`, simply double-click on the file, and it will silently run in the background, watching for changes in the default playlist opened by PotPlayer.

   - **Running on Startup:** To automatically run the PotPlayer Playlist Watcher on startup, you can add `hidePotWatcher.vbs` to the startup folder. Navigate to the following directory:
     ```
     C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
     ```
     Replace `username` with your actual username. Then, copy `hidePotWatcher.vbs` into this folder. Upon system startup, `hidePotWatcher.vbs` will execute automatically, ensuring that the PotPlayer Playlist Watcher is always running in the background, ready to detect playlist changes.


## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
Special thanks to the developers of PotPlayer for creating such a versatile media player, as well as to the creator(s) of the potplayer library and to the open-source community for their invaluable contributions.
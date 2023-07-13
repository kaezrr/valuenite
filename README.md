# Valuenite
A simple python program to find out the total value of your Playnite library based on Steam prices. If a game is not available on Steam or Steam API doesn't recognise the name, it's value will not be considered.

### Prerequisites
To use this program, you need to have a `playnite_data.csv` file that contains the names of all your games in your Playnite library.

To obtain this file, follow these steps:
- Install the [**Library Exporter Advanced**](https://github.com/darklinkpower/PlayniteExtensionsCollection) extension by *darklinkpower* in Playnite.
- Open Playnite and go to the top right corner.
- Click on *Extensions -> Library Exporter Advanced -> Open export window*.
- Rename the exported CSV file to `playnite_data.csv` and place it in the same directory as app.py.

Run `app.py` and enjoy!

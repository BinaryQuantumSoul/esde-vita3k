# ES-DE - Vita3K
This simple python script (`main.py`) generates `.psvita` files that can then be read by EmulationStation in order to fill its library.

Simply run the script, specify rom directory and if the roms are named with title names or title ids. The script will then pick the other one from json database and generate the corresponding files.

> [!Note]
> This is not perfect as I was not able to find a better title-name/title-id list. Some game titles are not in english and some titles will not scrape.

Process is detailed in [ES-DE PSVita guide](https://gitlab.com/es-de/emulationstation-de/-/blob/master/USERGUIDE.md#sony-playstation-vita).

## Build database
Simply run `database_scrape.py`. The data is scraped from two google sheets:
- [Vita Games DB - EU](https://docs.google.com/spreadsheets/d/1SvfQrAavckZH9fBCo48bpfIx3jWpMDUOCPnDWMekMBg/edit)
- [Vita Title IDs (2020/02/20)](https://docs.google.com/spreadsheets/d/1muoSZ-ZyJfyb1D5Sd26ZRr2cwDyFmPz5aLyFFe9JELQ/edit)

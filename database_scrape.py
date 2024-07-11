import wget
import json
import os

urls =  [
    'https://docs.google.com/spreadsheets/d/1muoSZ-ZyJfyb1D5Sd26ZRr2cwDyFmPz5aLyFFe9JELQ/gviz/tq?tqx=out:json',
    'https://docs.google.com/spreadsheets/d/1SvfQrAavckZH9fBCo48bpfIx3jWpMDUOCPnDWMekMBg/gviz/tq?tqx=out:json',
    'https://docs.google.com/spreadsheets/d/18vnzs4VnqKlqqIgHXenqQjMq2ygMUnfc28WKSYC7-vo/gviz/tq?tqx=out:json'
]
game_data = {}

for url in urls:
    wget.download(url, 'game-data-in.json')

    with open('game-data-in.json', 'r') as file:
        content = file.read()
        content = content.lstrip('/*O_o*/\ngoogle.visualization.Query.setResponse(')
        content = content.rstrip(');')

        data = json.loads(content)
        for row in data['table']['rows'][1:]:
            game_data[row['c'][0]['v'].replace('-', '')] = row['c'][1]['v'].replace(':', ' -').replace('™', '')

    os.remove('game-data-in.json')

with open('game-data.json', 'w') as file:
    json.dump(game_data, file, indent=4)
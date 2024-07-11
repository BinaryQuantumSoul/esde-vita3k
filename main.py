#set es-de psvita rom directory here
game_dir = ''

import os
import json

with open('game-data.json', 'r') as file:
    game_data = json.load(file)

def prompt_non_empty(text: str):
    response = None
    while not response:
        response = input(f"{text}")
    return response

def prompt_in_set(text: str, sset):
    set_string = "/".join(sset)

    response = None
    while response not in sset:
        response = input(f"{text} ({set_string}) ").lower()
    return response

def prompt_yes_no(text: str):
    return prompt_in_set(text, ['y', 'n']) == 'y'

if __name__ == "__main__":
    if not game_dir:
        game_dir = prompt_non_empty('Please provide vita es-de rom directory: ')
    is_name = prompt_in_set('Are the files named with title-name (1) or title-id (2) ? ', ['1','2']) == '1'

    if prompt_yes_no(f'Proceed with FILENAMES: {"title-name" if is_name else "title-id"}, DIRECTORY: {game_dir} ?'):
        files = [f.split('.')[0] for f in os.listdir(game_dir) if os.path.isfile(os.path.join(game_dir, f))]
        title_ids = None
        title_names = None

        if is_name:
            title_names = files
            reverse_data = {v:k for k,v in game_data.items()}
            title_ids = [reverse_data[key] for key in title_names]
        else:
            title_ids = files
            title_names = [game_data[key] for key in title_ids]

        for title_id, title_name in zip(title_ids, title_names):
            print(f"Processing {title_id}: {title_name}")

            with open(os.path.join(game_dir, f"{title_name}.psvita"), "w") as file:
                file.write(title_id)
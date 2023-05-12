from io import BytesIO
from tkinter import messagebox
import requests
import random
from PIL import Image


def get_answer_from_api():
    aid = random.randrange(1, 1016)
    api_pokemon = f"https://pokeapi.co/api/v2/pokemon/{aid}/"

    pokemon_response = requests.get(api_pokemon)
    if pokemon_response.status_code == 200:
        return pokemon_response.json()
    else:
        return "Error: Unable to download weather information"


def save_pokemon_img_to_file(pokemon_url, pokemon_name):
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        response = requests.get(pokemon_url)
        img = Image.open(BytesIO(response.content))
        img.save(rf"D:\Pokemons\{pokemon_name}.png")
        return rf"D:\Pokemons\{pokemon_name}.png"


def find_pokemon(json_pokemon):
    if json_pokemon != "Error: Unable to download weather information":
        sprites = json_pokemon['sprites']
        imag = sprites['front_default']
        path = save_pokemon_img_to_file(imag, json_pokemon['name'])
        return path
    else:
        error = json_pokemon
        messagebox.showerror(error)

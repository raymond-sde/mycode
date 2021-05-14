#!/usr/bin/env python3

# imports always go at the top of your code
import requests


def main():
    pokemon_name = input("Name a pokemon\n>")
    pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()

    img_url = pokeapi["sprites"]["front_default"]
    img_data = requests.get(img_url).content

    with open(f"{pokemon_name}.png", "wb") as out_file:
        out_file.write(img_data)

    print("URL: ", img_url)
    print("Game Indices Count: ", len(pokeapi["game_indices"]))

    print("All Moves:")

    for pokedict in pokeapi["moves"]:
        print(pokedict["move"]["name"])


main()

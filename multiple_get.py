#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()

        # The name of the character
        name = got_dj['name']

        # The name(s) of books the character appeared in
        books = [requests.get(book).json()['name'] for book in got_dj['books']]
        # books = ""
        # for book in got_dj['books']:
        #     bookresp = requests.get(book).json()
        #     books += bookresp['name']

        # The name(s) of allegiances the character has (if any)
        allegiances = [requests.get(allegiance).json()['name'] for allegiance in got_dj['allegiances']]
        # allegiances = ""
        # for allegiance in got_dj['allegiances']:
        #     allegianceresp = requests.get(allegiance).json()
        #     allegiances += allegianceresp['name']

        print(f"The name of the character: {name}")
        print(f"The name(s) of books the character appeared in: {', '.join(books)}")
        print(f"The name(s) of allegiances the character has (if any): {', '.join(allegiances)}")

if __name__ == "__main__":
        main()

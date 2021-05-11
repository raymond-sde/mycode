#!/usr/bin/env python3
# inspired by programmer meme https://i.redd.it/n3g19svtsg211.jpg

people = {
    1: {
        "title": "my mom",
        "answer": "play games all day",
        "url": "https://res.cloudinary.com/drtxi16qr/image/upload/v1620762870/programmer_meme/mom_ea0pse.png"
    },
    2: {
        "title": "my friends",
        "answer": "take apart computers",
        "url": "https://res.cloudinary.com/drtxi16qr/image/upload/v1620762870/programmer_meme/friends_qbtrmq.png"
    },
    3: {
        "title": "society",
        "answer": "live a sedentary lifestyle in my moms basement",
        "url": "https://res.cloudinary.com/drtxi16qr/image/upload/v1620762870/programmer_meme/society_g8w3tp.png"
    },
    4: {
        "title": "artists",
        "answer": "code with aweful design choices",
        "url": "https://res.cloudinary.com/drtxi16qr/image/upload/v1620762869/programmer_meme/artists_gernsm.png"
    },
    5: {
        "title": "I",
        "answer": "enter the matrix",
        "url": "https://res.cloudinary.com/drtxi16qr/image/upload/v1620765726/programmer_meme/i_lrsbhu.png"
    },
    6: {
        "title": "actual",
        "answer": "bang my head on errors all day",
        "url": "https://res.cloudinary.com/drtxi16qr/image/upload/v1620765731/programmer_meme/actual_ecd2qo.png"
    },
}

def print_menu():
    people_len = len(people.keys())
    h2 = "  " # indentation for sub-headings
    h3 = h2 * 2 # indentation for sub-heading items

    print("-" * 25)
    print("What I do as a Programmer")
    print(f"{h2}What ___ think(s) I do.")

    for i, person in enumerate(people.keys()):
        title = person["title"]

        if person["title"] != "actual":
            print(f"{h3}[{i + 1}] {person['title']}")

    print(f"{h2}What I actually do")
    print(f"{h3}[{people_len}] find out")
    print(f"{h2}Other Options")
    print(f"{h3}[{people_len + 1}] quit")
    print("-" * 25)

def start():
    answer = " "

    while answer != "7":
        MIN_RANGE = 1
        MAX_RANGE = 7

        print_menu()
        answer = input("Your answer--> ")

        if answer == "1":
            print("1")
        elif answer == "2":
            print("2")
        elif answer == "3":
            print("3")
        elif answer == "4":
            print("4")
        elif answer == "5":
            print("5")
        elif answer == "6":
            print("6")
        elif answer == "7":
            print("7")
        else:
            print(f"Invalid input. Please enter a number {MIN_RANGE}-{MAX_RANGE}")

start()

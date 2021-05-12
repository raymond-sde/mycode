farms = [
    {
        "name": "NE Farm",
        "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"],
    },
    {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
    {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
]

# function 1
# Write a for loop that returns all the animals from the NE Farm!
print("function 1\n")

for animal in farms[0]["agriculture"]:
    print(animal)

# function 2
# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm.
print("\nfunction 2\n")
print("0. NE Farm")
print("1. W Farm")
print("2. SE Farm")

farm_input = int(input("Choose a farm. (0, 1, or 2)\n>"))

for animal in farms[farm_input]["agriculture"]:
    print(animal)

# function 3
# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.
print("\nfunction 3\n")

farm_input = int(input("Choose a farm. (0, 1, or 2)\n>"))
veg = ["carrots", "celery"]


for animal in farms[farm_input]["agriculture"]:
    if animal not in veg:
        print(animal)

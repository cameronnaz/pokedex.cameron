import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)

print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
for item in (data):
    print(item['name'])
# Add a language choice feature and print the pokemons name based on the user input
language = input("What language do you want")
for item in (data):
    print(item['name'][language])
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def type():
    x = []
    pokemon = 0
    pokemon_type = input("What pokemon type would you like")
    for item in (data):
        if pokemon_type.title() in item['type']:
            print(item['name'][language])
            pokemon +=1
    if pokemon == 0:
        print("No pokemon was found")
type()
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def name():
    search = input("Find a pokemon")
    for item in (data):
        if search in item['name']['english'].lower():
            print(item['name']['english'])
name()
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

 
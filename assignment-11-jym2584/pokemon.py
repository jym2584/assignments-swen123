'''Mon, Oct 26: SI Session
'''
class Pokemon:
    name = "None"
    Type = "None"
    health = 0
    level = 0
    move1 = "None"
    move2 = "None"
    move3 = "None"
    move4 = "None"

my_pokemon = Pokemon()

def print_my_pokemon(pokemon):
    print("\nPOKEMON:",pokemon.name, 
    "\nType:", pokemon.Type, 
    "\nHealth:", pokemon.health,
    "\nLevel:", pokemon.level, 
    "\nMove 1:", pokemon.move1, 
    "\nMove 2:", pokemon.move2, 
    "\nMove 3:", pokemon.move3, 
    "\nMove 4:", pokemon.move4)

#print_my_pokemon(my_pokemon)

def make_team():
    # First pokemon
    pokemon = Pokemon()
    pokemon.name = "Prof. Herring"
    pokemon.Type = "Everything"
    pokemon.health = 99999999
    pokemon.level = 999
    pokemon.move1 = "Teach"
    pokemon.move2 = "Fail Student"
    pokemon.move3 = "Use TDD"
    pokemon.move4 = "Blame Bobby"
    #print_my_pokemon(pokemon)

    pokemon2 = Pokemon()
    pokemon2.name = "Litwick"
    pokemon2.Type = "Fire and Ghost"
    pokemon2.health = 5
    pokemon2.level = 1
    pokemon2.move1 = "Ember"
    pokemon2.move2 = "Shadow Ball"
    pokemon2.move3 = "Tackle"
    pokemon2.move4 = "Hyperbeam"
    #print_my_pokemon(pokemon2)

    pokemon3 = Pokemon()
    pokemon3.name = "Patrick"
    pokemon3.Type = "Fire (cause lit)"
    pokemon3.health = 99999999
    pokemon3.level = 100
    pokemon3.move1 = "Play Kahoot Game"
    pokemon3.move2 = "Sleep"
    pokemon3.move3 = "Watch Sports"
    pokemon3.move4 = "Swear"
    #print_my_pokemon(pokemon3)

    return pokemon, pokemon2, pokemon3

def main():
    the_dict = dict()
    pokemon, pokemon2, pokemon3 = make_team()
    print_my_pokemon(pokemon)
    print_my_pokemon(pokemon2)
    print_my_pokemon(pokemon3)
                            # Type, Health, Level, Move1, Move2, Move3
    #the_dict[pokemon.name] = [pokemon.Type, pokemon.health, pokemon.level, pokemon.move1, pokemon.move2, pokemon.move3, pokemon.move4]
    #the_dict[pokemon2.name] = [pokemon2.Type, pokemon2.health, pokemon2.level, pokemon2.move1, pokemon2.move2, pokemon2.move3, pokemon2.move4] 
    #the_dict[pokemon3.name] = [pokemon3.Type, pokemon3.health, pokemon3.level, pokemon3.move1, pokemon3.move2, pokemon3.move3, pokemon3.move4]
    the_dict[pokemon.name] = pokemon
    the_dict[pokemon2.name] = pokemon2
    the_dict[pokemon3.name] = pokemon3
    #print(the_dict)
    print(the_dict['Patrick'].health)

main()
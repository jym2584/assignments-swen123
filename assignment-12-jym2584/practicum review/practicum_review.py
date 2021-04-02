import csv
# Number 1
def occurrences(filename):
    character_count = dict()
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            for each_word in line[:2]:
                for character in each_word:
                    if character not in character_count:
                        character_count[character] = 1
                    else:
                        character_count[character] += 1
    return character_count

def occurrences_from_string(string):
    character_count = dict()
    for letter in string:
        if letter not in character_count:
            character_count[letter] = 1
        else:
            character_count[letter] += 1
    return character_count
 # Number 2
def union(dict1, dict2):
    unique_values = dict()
    for key in dict1:
        unique_values[key] = dict1[key]
    for key in dict2:
        unique_values[key] = dict2[key]

    return unique_values


# Number 3
def unique_letters(string):
    unique_list = set()
    for char in string:
        unique_list.add(char)
    print("Number of unique letters:", len(unique_list))
    return len(unique_list)

def set_intersection(set1, set2):
    intersection = set()
    for element in set1:
        if element in set2:
            intersection.add(element)
    return intersection

# Number 5
class Circle:
    __slots__ = ["__radius", "__color"]
    def __init__(self, radius, color):
        self.__radius = radius
        self.__color = color
 
# Number 6
class Player:
    __slots__ = ["__name", "__team", "__score"]
    def __init__(self, name, team, score):
        self.__name = name
        self.__team = team
        self.__score = score
    
    def get_name(self):
        return self.__name

    def get_team(self):
        return self.__team

    def get_score(self):
        return self.__score

    def __repr__(self):
        result = ''
        result += 'Player =' + self.__name + "\n"
        result += 'Player =' + self.__team + "\n"
        result += 'Player =' + str(self.__score) + "\n"
        return result

# Number 7
def add_player(filename):
    players = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader: # for record in reader
            players.append(Player(line[0], line[1], line[2]))
    return players

# Number 8
def print_winners(players):
    teams = dict()
    for player in players:
        if player.get_team() not in teams: # If there are no teams
            teams[player.get_team()] = 0 # Add each team (Blue, Red, Green) to the dictionary
            print("Not in dictionary", teams[player.get_team()])
        else:                   # Otherwise sum up all of the scores from each team
            teams[player.get_team()] += int(player.get_score())
            print("In dictionary", teams[player.get_team()])

    print(teams)

    scores = 0
    winning_team = ""
    for score in teams.keys():
        if teams[score] > scores:
            scores = teams[score]
            winning_team = score
    
    '''player_dict
    player's name: score
    '''
    print("Winning team", winning_team, "with score", scores)
    player_dict = dict()
    for player in players: # For each player in the dictionary
        if player.get_team() == winning_team: # IF the player is on the winning team
            #print(player.get_score()) # Prints up the sum of all player scores regardless of their team (testing)
            if player not in player_dict: # IF the player is not on player_dict
                player_dict[player.get_name()] = int(player.get_score()) # Add them to the dictionary
                print(player.get_name() + "   Print 1 (if player not in player_dict):", player_dict[player.get_name()])
            else: # Otherwise if it's now valid then add the sum of their scores to the dictionary
                player_dict[player.get_name()] += int(player.get_score())
                print(player.get_name() + "   Print 2 (if player in player_dict):", player_dict[player.get_name()])
                        # Tim: 1150, Jim: 840, Megan: 1
    return player_dict


def main():
    filename = "practicum review/TeamData.csv"
    string = "abcabc1234325sddasfjfjj"
    dict1 = {'one':1, 'Two': 2}
    dict2 = {'tree': 't'}
    set1 = set("Hello")
    set2 = set("Goodby")

    # Number 1
    print("Occurrences from filename",occurrences(filename))
    print("Occurrences from string", occurrences_from_string(string))
    print() # Number 2
    print("Union", union(dict1, dict2))
    print() # Number 3
    unique_letters(string)
    print() # Number 4
    print(set_intersection(set1, set2))
    print() # number 7
    players = add_player(filename)
    print() # Number 8
    print(print_winners(players))

if __name__ == "__main__":
    main()
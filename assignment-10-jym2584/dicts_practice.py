"""
Practice problems for SWEC 123.07
Topic: Python Dictionaries
"""

def create_dicts(filename):
    # create three dictionaries 
    # one with their name as the key and their team(s) as the value 
    # *HINT* Some players have played for multiple teams
    # one with their name as the key and their amount of rings as the value 
    # one with their name as the key and their status as the value
    team = {}
    ring = {}
    status = {}

    with open(filename) as file:
        for line in file:
            line = line.strip().split(", ")
            team[line[0]] = line[1]
            ring[line[0]] = line[2]
            status[line[0]] = line[3]
    print(team)
    print(ring)
    print(status)
    return team, ring, status
def find_loyalty(nba_players):
    # find and print out the players who only stayed with one team
    for key in nba_players:
        if len(nba_players[key].split(" ")) == 1:
            print(key)
    pass

def multiple_teams(nba_players):
    # find and print out the players who played for multiple teams
    
    pass

def find_champs(player_rings):
    # find and print out the players who have won championship(s)
    
    pass

def find_active(player_status):
    # find and print out the players who are currently active
    
    pass

def main():
    filename = "nba_players.txt"
    create_dicts(filename)
    team, ring, status = create_dicts(filename)
    find_loyalty(team)
    pass

if __name__ == "__main__":
    main()
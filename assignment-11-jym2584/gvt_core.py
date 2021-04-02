import random

COMMON = 1
UNCOMMON = 2
RARE = 3
LEGENDARY = 4

RARITY_STRINGS = {COMMON:"C", UNCOMMON:"U", RARE:"R", LEGENDARY:"L"}

class Colors:
    '''Strings for adding our colors to the card in a (hopefully) efficient way
    '''
    # For our card rarity
    common = "\u001b[38;5;7m"
    uncommon = "\u001b[38;5;10m"
    rare = "\u001b[38;5;26m"
    legendary = "\u001b[38;5;130m"

    # For our card health
    green = "\u001b[38;5;28m"
    yellow = "\u001b[38;5;11m"
    red = "\u001b[38;5;9m"

    # Always have to end a color with Colors.end
    end = "\033[0m"

class Player:
    '''Class for player
    @param name, The player's name
    @param mana, How many resource points (or mana) the player has
    @param deck, Deck of GvT cards (not sure what this really means)
    @param hand, hand of cards
    @param cards_on_board, the cards the player currently has in their hand
    @param discarded_cards, discarded cards after losing
    '''
    __slots__ = ["name", "score", "mana", "deck", "hand", "cards_on_board", "discarded_cards"]
    def __init__ (self, name):
        self.name = name
        self.score = 100
        self.mana = 0
        self.deck = list()
        self.hand = list()
        self.cards_on_board = list()
        self.discarded_cards = list()

class Power:
    ''' Class for the card's power
    @param name, The power's name
    @param description, The power's ability description
    @param execute, Some function we are going to execute
    @param single_use, If the card is a single use or not (True/False)
    '''
    __slots__ = ["name", "description", "execute", "single_use"]
    
    def __init__ (self, name, description, execute, single_use = False):
        self.name = name
        self.description = description
        self.execute = execute
        self.single_use = single_use


card_powers = {"MagicMissile": Power("Magic Missile", "Does a little pew pew pew", "Some function passed in without using strings"),
               "Battlecry": Power("Battlecry", "Gain +1 attack as long as the health is full", "Some function", True)
               }

class Card:
    '''Class for our cards
    @param name, The card's name
    @param rarity, The card's rarity; COMMON, UNCOMMON, RARE, LEGENDARY
    @param faction, The card's faction
    @param damage, How many damage the card deals
    @param health, The health the card currently has
    @param power, If the card has any special powers
    @param health_init, The card's initial health, used to track the card's health status
    @param total, splits up how much health/damage the card should have given a value
    '''
    __slots__ = ["name", "cost", "rarity", "faction", "damage", "health", "power", "health_init"]

    def __init__ (self, name, rarity, faction, power = None):
        self.name = name
        self.cost = 0
        self.rarity = rarity
        self.faction = faction
        self.damage = 0
        self.health = 1
        self.power = power
        self.health_init = 0

        total = 0
        if rarity == COMMON:
            total = 8
            self.cost = random.randint(1, 3)
            self.damage = random.randint(0,total-1)
            self.health = (total - self.damage)
            self.health_init = self.health
        if rarity == UNCOMMON:
            total = 12
            self.cost = random.randint(2, 5)
            self.damage = random.randint(0,total-1)
            self.health = (total - self.damage)
            self.health_init = self.health
        if rarity == RARE:
            total = 16
            self.cost = random.randint(4, 7)
            self.damage = random.randint(0,total-1)
            self.health = (total - self.damage)
            self.health_init = self.health
        if rarity == LEGENDARY:
            total = 24
            self.cost = 10
            self.damage = random.randint(0,total-1)
            self.health = (total - self.damage)
            self.health_init = self.health

def print_card(card, end = " "):
    ''' Pretty prints the card
    @param output, formatting the card and using ansi color values based on rarity and health
    
    Format: HEALTH, COST, ATTACK, HEALTH
    '''
    output = "["
    if card.rarity == COMMON:
        output += Colors.common
    elif card.rarity == UNCOMMON:
        output += Colors.uncommon
    elif card.rarity == RARE:
        output += Colors.rare
    elif card.rarity == LEGENDARY:
        output += Colors.legendary 
    
    output += RARITY_STRINGS[card.rarity]

    if card.power == None:
        output += "N"
    else:
        output += card.power.name[0]

    output += Colors.end

    output +=" {:0>2d}".format(card.cost)
    output +=" {:0>2d}".format(card.damage)

    if card.health == card.health_init:
        output += Colors.green
    elif card.health < card.health_init and card.health > card.health_init / 2 or card.health == card.health_init / 2:
        output += Colors.yellow
    elif card.health < card.health_init / 2:
        output += Colors.red

    output +=" {:0>2d}".format(card.health)
    output += Colors.end + "]"
    print(output, end=end)
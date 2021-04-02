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
    __slots__ = ["__name", "__score", "__mana", "__deck", "__hand", "__cards_on_board", "__discarded_cards"]
    def __init__ (self, name):
        self.__name = name
        self.__score = 100
        self.__mana = 0
        self.__deck = list()
        self.__hand = []
        self.__cards_on_board = list()
        self.__discarded_cards = list()

    
    def get_name(self):
        '''Gets the name of the player
        '''
        return self.__name

    def get_score(self):
        '''Gets the score of the player
        '''
        return self.__score

    def get_hand(self):
        '''Gets the hand of the player
        '''
        return self.__hand

    def add_to_hand(self, card):
        '''Appends the card to the player's hand and sorts it by rarity and cost
        '''
        self.__hand.append(card)
        self.__hand.sort()

    def remove_from_hand(self, card):
        '''Removes a card from the player
        '''
        self.__hand.remove(card)

    def add_score(self, amount):
        '''Adds a specified amount to the player's score
        '''
        self.__score += amount

    def get_discard(self):
        '''Grabs a list of discarded cards
        '''
        return self.__discarded_cards
    
    def add_to_discard(self, card):
        '''Adds a card to the discard pile
        '''
        self.__discarded_cards.append(card)

    def battle(self, card, enemy, enemy_card):
        '''This is where we attack our opponent!
            1. Parses through the enemy's hand
            2. If the enemy's card exists, then we attack it based on how much
                damage the attackee card's deals
            3. take_damage also does a quick check to add the enemy's card to
                the discard pile if it's below 0 health

        @param card, the player's card that they want to attack with
        @param enemy, we want to target the opponent
        @param enemy_card, we want to use our card to attack the enemy's card
        '''
        if len(self.__hand) > 0:
                card = self.__hand[card]
                for hand in enemy.get_hand():
                    print(enemy.get_hand()[enemy_card].get_name())
                    if enemy.get_hand()[enemy_card].get_name() == hand.get_name():
                            print("Attacking", enemy.get_hand()[enemy_card].get_name(), "from", enemy.get_name())
                            hand.take_damage(card.get_damage(), enemy)
            # Implemented discarding card if health is 0 on the Card class (take_damage)
    
    def add_mana(self):
        '''Adds the mana of the player by 1
        '''
        self.__mana += 1

    def check_score(self):
        '''If the player's score is 0, then return True
        '''
        if self.__score == 0:
            return False # Player is dead
        else:
            return True # Player is still alive!


class Power:
    ''' Class for the card's power
    @param name, The power's name
    @param description, The power's ability description
    @param execute, Some function we are going to execute
    @param single_use, If the card is a single use or not (True/False)
    '''
    __slots__ = ["__name", "__description", "__power_func", "__single_use", "__used"]
    
    def __init__ (self, name, description, power_func, single_use = False):
        self.__name = name
        self.__description = description
        self.__power_func = power_func # function, not a class
        self.__single_use = single_use
        self.__used = False

    def get_name(self):
        '''Gets the name of the power
        '''
        return self.__name
    
    def get_description(self):
        '''Gets the description of the power
        '''
        return self.__description

    def get_power(self):
        '''Gets the power function of the power
        '''
        return self.__power_func
    
    def get_used(self):
        '''Gets True/False if used
        '''
        return self.__used
    
    def get_single_use(self):
        '''Grabs True/False if the power is a first time
        '''
        return self.__single_use

    def activate(self, player, card):
        '''Activates the power's function!
        '''
        if self.__used and self.__single_use:
            print("This card has already been activated")
            return False
        else:
            self.__power_func(player, card)
            self.__used = True
            return True

    def __eq__(self, other):
        '''Checks for duplicate powers
        '''
        if type(self) == type(other):
            return self.__name == other.__name and \
                self.__power_func == other.__power_func
        else:
            return False

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
    __slots__ = ["__name", "__cost", "__rarity", "__faction", "__damage", "__health", "__power_func", "__health_init"]

    '''Creating initting the power instead of adding, when creating card
    '''
    def __init__ (self, name, rarity, faction, power_func = None):
        self.__name = name
        self.__cost = 0
        self.__rarity = rarity
        self.__faction = faction
        self.__damage = 0
        self.__health = 1
        self.__power_func = power_func
        self.__health_init = 0

        total = 0
        if rarity == COMMON:
            total = 8
            self.__cost = random.randint(1, 3)
            self.__damage = random.randint(0,total-1)
            self.__health = (total - self.__damage)
            self.__health_init = self.__health
        if rarity == UNCOMMON:
            total = 12
            self.__cost = random.randint(2, 5)
            self.__damage = random.randint(0,total-1)
            self.__health = (total - self.__damage)
            self.__health_init = self.__health
        if rarity == RARE:
            total = 16
            self.__cost = random.randint(4, 7)
            self.__damage = random.randint(0,total-1)
            self.__health = (total - self.__damage)
            self.__health_init = self.__health
        if rarity == LEGENDARY:
            total = 24
            self.__cost = 10
            self.__damage = random.randint(0,total-1)
            self.__health = (total - self.__damage)
            self.__health_init = self.__health
    
    def get_power(self):
        '''Gets the power function of the card
        '''
        return self.__power_func

    def add_power(self, power):
        '''Adds the power to the card
        '''
        self.__power_func = power

    def get_rarity(self):
        '''Grabs the rarity of the card
        '''
        return self.__rarity

    def get_cost(self):
        '''Grabs the cost of the card
        '''
        return self.__cost

    def get_name(self):
        '''Grabs the name of the card
        '''
        return self.__name

    def get_health(self):
        '''Grabs the health of the card
        '''
        return self.__health

    def get_damage(self):
        '''Grabs the damage of the card
        '''
        return self.__damage
        
    def add_health(self, amount):
        '''Adds a specified amount of health to the card
            Prevents the card from healing past its full health
        '''
        if self.__health == self.__health_init: # If the health of the card is full
            print("Cannot heal ",self.__name, " (has full health)" ,sep="")
            pass                                # Do not add any more health points
        else:
            print("Healed ", self.__name, " ", amount, " HP. (Now has: ", self.__health + amount, " HP)",  sep="")
            self.__health += amount

    #def subtract_health(self, amount):
        #self.__health -= amount

    def activate(self, player): # Can pass in activate to check if it has a power, then the card activates at the start of each round
        '''Activates the power function if the card has a power
        Can be immediately ran at the start of the round if they have a power (assignment 12.1, problem 7a)        
        '''
        if self.__power_func != None:
            self.__power_func.activate(player, self)

    def take_damage(self, amount, player):
        ''' Card inflicting damage. 
        Also checks if the card's health is depleted then it gets removed to the player's discard pile
        '''
        self.__health -= amount
        print(self.__name, "current status", self)
        if self.__health < 0: # If the health is less than 0
            for hand in player.get_hand(): # For each card in the player's hand
                if hand.get_name() == self.__name: # If the card exists in the player's hand
                    print(self.__name, "has been defeated!") 
                    player.remove_from_hand(hand) # Remove the card from the player's hand
                    player.add_to_discard(hand) # Add the card to the discard pile
                    print("Added", hand.get_name(),"to", player.get_name(), "discard pile")
        else:
            pass

    ###########################################################


    def __str__(self):
        ''' Pretty prints the card
        @param output, formatting the card and using ansi color values based on rarity and health
        
        Format: HEALTH, COST, ATTACK, HEALTH
        '''
        output = "["
        if self.__rarity == COMMON:
            output += Colors.common
        elif self.__rarity == UNCOMMON:
            output += Colors.uncommon
        elif self.__rarity == RARE:
            output += Colors.rare
        elif self.__rarity == LEGENDARY:
            output += Colors.legendary 
        
        output += RARITY_STRINGS[self.__rarity]

        if self.__power_func == None:
            output += "N"
        else:
            output += self.__power_func.get_name()[0]

        output += Colors.end

        output +=" {:0>2d}".format(self.__cost)
        output +=" {:0>2d}".format(self.__damage)

        if self.__health == self.__health_init:
            output += Colors.green
        elif self.__health < self.__health_init and self.__health > self.__health_init / 2 or self.__health == self.__health_init / 2:
            output += Colors.yellow
        elif self.__health < self.__health_init / 2:
            output += Colors.red

        output +=" {:0>2d}".format(self.__health)
        output += Colors.end + "]"
        output += " "
        return output

    def __repr__(self):
        return print("Hello")

    def __eq__(self, other):
        '''Checks for duplicates based on rarity, cost, damage, health and power function
        '''
        if type(self) == type(other):
            return self.__rarity == other.__rarity and \
                self.__cost == other.__cost and \
                    self.__damage == other.__damage and \
                        self.__health == other.__health and \
                            self.__power_func == other.__power_func
        else:
            return False
    
    def __lt__(self, other):
        '''Sorts the card by rarity and cost
        '''
        if type(self) != type(other):
            return False
        if self.__rarity == other.__rarity:
            return self.__cost < other.__cost
        else:
            return self.__rarity < other.__rarity
    
    def __hash__(self):
        '''Hashes each card
        '''
        return (self.__health_init * 31**3) + \
            (self.__damage * 31 ** 2) + \
                (self.__cost * 31 ** 2) + \
                self.__rarity

def regeneration(player, card):
    ''' Adds 1 health to the card if it exists on the player's hand
    '''
    for hand in player.get_hand():
        print("Hand name:", hand.get_name())
        if hand == card:
            card.add_health(1)
            #print(card.get_name(), "healed for 1 health!")
            return True
        else:
            print("Cannot heal because")
            print(player.get_name(), "does not have the card", card.get_name(), "in their hand!")

def first_aid (player, card):
    ''' Adds 5 score to the player if the card exists on the player
    '''
    print(card.get_name(), "added 5 health to", player.get_name())
    player.add_score(5)
    print("Score is now", player.get_score())
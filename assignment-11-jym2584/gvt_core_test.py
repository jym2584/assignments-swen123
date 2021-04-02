from gvt_core import *

def test_player():
    #Setup
    name = "Pumpkin"

    #Invoke
    player1 = Player(name)
    
    #assert
    assert name == player1.name
    assert 0 == player1.mana
    assert 100 == player1.score
    assert [] == player1.hand
    assert [] == player1.deck
    assert [] == player1.cards_on_board
    assert [] == player1.discarded_cards

def test_card():
    #Setup
    random.seed(1)
    name = "Murlok"
    rarity = 1
    faction = "Trolls"
    murlok = Card(name, rarity, faction)

    assert name == murlok.name
    assert 1 == murlok.cost
    assert rarity == murlok.rarity
    assert faction == murlok.faction
    assert 1 == murlok.damage
    assert 7 == murlok.health
    assert None == murlok.power

def test_power():
    #setup
    name = "Deathrattle"
    description = "Upon death, summon 2 Murloks with 1/1"
    execute = None
    
    deathrattle = Power(name, description, execute)

    assert name == deathrattle.name
    assert description == deathrattle.description
    assert execute == deathrattle.execute
    assert False == deathrattle.single_use



murlok = Card("Murloc Raider", 1, "Trolls")
print_card(murlok)
murlok.rarity = 2
murlok.health = murlok.health - 1
print_card(murlok)
murlok.rarity = 3
murlok.health = murlok.health // 2
murlok.power = card_powers["Battlecry"]
print_card(murlok)
murlok.rarity = 4
murlok.health = 0
#print(card_powers["MagicMissile"].name)
murlok.power = card_powers["MagicMissile"]
#print(murlok.power.name)
print_card(murlok)
#print(Colors.uncommon + "Hello", Colors.end)
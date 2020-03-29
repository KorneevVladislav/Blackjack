import Functions
import Players

def Game(decks, players):

    # Shuffle the given cards and give them all values
    card_translate = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}
    cards = Functions.Shuffle(decks)

    while len(cards) > (players + 1) * 6:
        
        # Players play their turns
        gcards = [cards[0], cards[1]]
        del cards[0]
        del cards[0]
        player_1 = Players.Player(card_translate, 1, cards, gcards)
        
        # Deler's turn
        gcards = [cards[0], cards[1]]
        del cards[0]
        del cards[0]
        deler = Players.Deler(card_translate, cards, gcards)
        
        # For testing, write who won and lost
        if deler > player_1:
            print("Player 1 Lost")
        elif deler < player_1:
            print("Player 1 Won")
        else:
            print("Player 1 tied with the deiler")
        print("----------------------------------------------------------------------------")
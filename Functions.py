from random import randint
import Players

def Find(listt, thing):
    for i in range(len(listt)):
        if listt[i] == thing:
            return i

    return -1

def Shuffle(decks):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    copy_cards = cards * 4 * decks
    newcards = []

    while len(copy_cards) > 0:
        card = randint(0, len(copy_cards) - 1)
        newcards.append(copy_cards[card])
        del copy_cards[card]

    return newcards
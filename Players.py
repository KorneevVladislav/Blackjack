import Functions

# Deler's turn. Less complex AI.
def Deler(card_translate, cards, gcards):
    # Finds starting value of cards. If 21 outomaticaly wins
    summ = int(card_translate[gcards[0]]) + int(card_translate[gcards[1]])
    printedcards = ", ".join(gcards)
    print("Dieler:         Cards: (" + printedcards + ")" + " " * (17 - len(printedcards)) + "Total Sum: " + str(summ))
    if summ == 21:
        return 23
    
    # Loop for drawing cards
    while summ <= 17:
        summ += int(card_translate[cards[0]])
        gcards.append(cards[0])
        del cards[0]

        # If over, replaces Aces with ones
        if summ > 21:
            any_aces = Functions.Find(gcards, "A")
            if any_aces >= 0:
                gcards[any_aces] = "Ace: 1"
                summ -= 10

        # Prints results of the draw
        printedcards = ", ".join(gcards)
        print("Dieler:         Cards: (" + printedcards + ")      Total Sum: " + str(summ))
    
    # If over, loses, unless player is also over
    if summ > 21:
        return -1

    # Returns final result
    return summ

# Players, actualy kind of intelegent, need to know when to get out, how much to bet and how to split and double down
def Player(card_translate, pnum, cards, gcards):
    # Calculates starting amount in cards, prints it, if 21 then wins unless tha deler has 21
    summ = int(card_translate[gcards[0]]) + int(card_translate[gcards[1]])
    printedcards = ", ".join(gcards)
    print("Player " + str(pnum) + ":     Cards: (" + printedcards + ")     Total Sum: " + str(summ))
    if summ == 21:
        return 22

    # Draws cards untill reaches 14. Turns Aces to ones if over, needs to know how too double down and split
    while summ <= 14:
        summ += int(card_translate[cards[0]])
        gcards.append(cards[0])
        del cards[0]

        # If over 21 and has Aces
        if summ > 21:
            any_aces = Functions.Find(gcards, "A")
            if any_aces >= 0:
                gcards[any_aces] = "Ace: 1"
                summ -= 10
        
        # Prints result of the draw
        printedcards = ", ".join(gcards)
        print("Player " + str(pnum) + ":" + " " * (8 - len(str(pnum))) +"Cards: (" + printedcards + ")" + " " * (17 - len(printedcards)) + "Total Sum: " + str(summ))
    
    # If over 21 loses
    if summ > 21:
        return -2
    
    # Returns final result
    return summ
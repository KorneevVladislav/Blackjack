import Functions

def Deler(card_translate, cards, gcards):
    summ = int(card_translate[gcards[0]]) + int(card_translate[gcards[1]])
    printedcards = ", ".join(gcards)
    print("Dieler:         Cards: (" + printedcards + ")" + " " * (17 - len(printedcards)) + "Total Sum: " + str(summ))
    if summ == 21:
        return 23
    while summ < 17:
        summ += int(card_translate[cards[0]])
        gcards.append(cards[0])
        del cards[0]
        if summ > 21:
            any_aces = Functions.Find(gcards, "A")
            if any_aces >= 0:
                gcards[any_aces] = "Ace: 1"
                summ -= 10
        printedcards = ", ".join(gcards)
        print("Dieler:     Cards: (" + printedcards + ")      Total Sum: " + str(summ))
    if summ > 21:
        return -1
    return summ

def Player(card_translate, pnum, cards, gcards):
    summ = int(card_translate[gcards[0]]) + int(card_translate[gcards[1]])
    printedcards = ", ".join(gcards)
    print("Player " + str(pnum) + ":     Cards: (" + printedcards + ")     Total Sum: " + str(summ))
    if summ == 21:
        return 22
    while summ < 15:
        summ += int(card_translate[cards[0]])
        gcards.append(cards[0])
        del cards[0]
        if summ > 21:
            any_aces = Functions.Find(gcards, "A")
            if any_aces >= 0:
                gcards[any_aces] = "Ace: 1"
                summ -= 10
        printedcards = ", ".join(gcards)
        print("Player " + str(pnum) + ":" + " " * (8 - len(str(pnum))) +"Cards: (" + printedcards + ")" + " " * (17 - len(printedcards)) + "Total Sum: " + str(summ))
    if summ > 21:
        return -2
    return summ
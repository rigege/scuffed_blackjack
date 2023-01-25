import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards = []
dealer_cards = []

def drawCards():
    player_cards.append(cards[random.randint(0,12)])
    player_cards.append(cards[random.randint(0,12)])
    
    dealer_cards.append(cards[random.randint(0,12)])
    dealer_cards.append(cards[random.randint(0,12)])
    
    while (sum(dealer_cards) < 17):
        draw(dealer_cards)
    
    if (player_cards == [11, 11]):
        player_cards[0] = 1
    
def sum(hand):
    sum = 0
    for x in hand:
        sum += x
    
    return sum

def draw(hand):
    counter = 0
    hand.append(cards[random.randint(0,12)])
    
    if (sum(hand) > 21):
        while (counter < len(hand)):
            if(hand[counter] == 11) :
               hand[counter] = 1
            counter += 1
        
def printHand():
    print(f"Your cards are: {player_cards}")
    
def printHandD():
    print(f"The dealer's cards are: {dealer_cards}")
    
def checkCondition(hand):
    if (sum(hand) == 21 and sum(dealer_cards) != 21):
        printHandD()
        print("You win") 
        restart()
    elif (sum(hand) > 21 and sum(dealer_cards) <22):
        printHandD()
        print("You lose")
        restart()
    elif (sum(hand) < 21):
        getInput()
    else:
        printHandD()
        print("Draw")
        restart()
        
def getInput():
    if (sum(player_cards) < 21):
        answer = int(input("Type \"1\" to hit or \"2\" to stand: "))
        if (answer == 1):
            draw(player_cards)
            printHand()
            getInput()
        elif (answer == 2):
            printHandD()
            if (sum(player_cards) == sum(dealer_cards)):
                print("Draw")
            elif (sum(player_cards) < sum(dealer_cards) and sum(dealer_cards) < 22): 
                print("You lose")
                restart()
            else:
                print("You win")
                restart()
        else:
            print("Not a valid input")
            getInput()
    else:
        checkCondition(player_cards)
        
def restart():
    answer = int(input("Type \"1\" to restart: "))
    if (answer == 1):
        start()
    else:
        print("GG")

def start(): 
    print("-------------------------------------------------")   
    player_cards.clear()
    dealer_cards.clear()
    drawCards()
    printHand()
    checkCondition(player_cards)

start()
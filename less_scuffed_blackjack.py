import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_cards = []
dealer_cards = []

# draws 2 starting cards for the player and dealer, if the cards are [11,11], sets the hand to [1,11] instead, then prints the hand
def drawCards():
    player_cards.append(cards[random.randint(0,12)])
    player_cards.append(cards[random.randint(0,12)])
    
    if (player_cards == [11,11]):
        player_cards[0] = [1,11]
    
    dealer_cards.append(cards[random.randint(0,12)])
    dealer_cards.append(cards[random.randint(0,12)])
    
    if (dealer_cards == [11,11]):
        dealer_cards[0] = [1,11]
        
    while (sum(dealer_cards) < 17):
        dealer_cards.append(cards[random.randint(0,12)])
        
    printHand()
        
# prints the hand of the player, then checks if game is won or not
def printHand():
    print(f"Your cards are {player_cards}")
    
    if (sum(player_cards) < 21):
        getInput()
        
    else:
        checkCondition()
    
# checks if game is won or not and prompts player accordingly
def checkCondition():
    if (sum(player_cards) == 21 and sum(dealer_cards)  != 21 or sum(player_cards) > sum(dealer_cards) and sum(player_cards) < 22):
        print(f"The dealer's cards are {dealer_cards}")
        print("You win")
        restart()
    elif (sum(player_cards) > 21 and sum(dealer_cards) < 22 or sum(player_cards) < sum(dealer_cards) and sum(dealer_cards) < 21):
        print(f"The dealer's cards are {dealer_cards}")
        print("You lose")
        restart()
    else:
        print(f"The dealer's cards are {dealer_cards}")
        print("It's a draw")
        restart()
        
# sums the values of the cards in a hand and returns the sum
def sum(hand):
    total = 0
    for x in hand:
        total += x  
        
    return total
    
# gets the players input for hit or stand and acts accordingly
def getInput():
    answer = int(input("Type 1 to hit or 2 to stand: "))
    
    if (answer == 1):
        player_cards.append(cards[random.randint(0,12)])
        counter = 0
        
        if (sum(player_cards) > 21):
            while (counter < len(player_cards)):
                if(player_cards[counter] == 11) :
                    player_cards[counter] = 1
                    break
                counter += 1
        
        printHand()
    elif (answer == 2):
        checkCondition()
    else:
        print("Not a valid input")
        getInput()

def restart():
    answer = int(input("Type 1 to restart: "))
    
    if (answer == 1):
        start()
    else:
        print("GG")

def start(): 
    print("--------------------------------------------")
    player_cards.clear()
    dealer_cards.clear()
    
    drawCards()
    
start()

from Card import Card
from Deck import Deck
import random

def showCards(cards):
    temp = [cards[0], cards[1], "[ ]", "[ ]"]
    print(temp)

numPlayers = int(input("How many players? "))

print(numPlayers)

players = []
playerNames = []

for i in range(numPlayers):
    players.append([None,None,None,None])
    playerNames.append(input("Player #" + str(i+1) + " What is your GTag? "))
deck = Deck()
deck.shuffle()

for i in range(len(players)):
    for j in range(len(players[i])):
        players[i][j] = deck.draw()

print(playerNames)
        
for i in range(len(players)):
    input("Ready, "+ playerNames[i] + "?")
    showCards(players[i])
    input("Done?")
    for j in range(25):
        print()
        
discardPile = []
discardPile.append(deck.draw())
hitList = []
for p in players:
    hitList.append(False)
running = True
while running:
    for i in range(len(players)):
        if hitList[i]:
            running = False
            break
        input("Ready, "+ playerNames[i] + "?")
        print("Top of discard Pile: " + str(discardPile[len(discardPile)-1]))
        move = input("A, look at the top\nB, Replace with discard\nC, Hit! ")
        move.lower()
        if move == "a":
            print("Top of deck: " + str(deck.peek()))
            discard = input("Do you want to discard? (Y/N) ")
            discard.lower()
            if discard == "y":
                discardPile.append(deck.draw())
            else:
                move2 = int(input("What card do you want to switch with? 1,2,3, or 4?"))
                move2 = move2 - 1
                discardPile.append(players[i][move2])
                players[i][move2] = deck.draw()
        elif move == "b":
            move2 = int(input("What card do you want to switch with? 1,2,3, or 4?"))
            move2 = move2 - 1
            temp = discardPile[len(discardPile)-1]
            discardPile[len(discardPile)-1] = players[i][move2]
            players[i][move2] = temp
        elif move == "c":
            hitList[i] = True
        print("Top of discard Pile: " + str(discardPile[len(discardPile)-1]))
        input("Done?")
        for j in range(25):
            print()

for i in range(len(players)):
    print(playerNames[i] + ":")
    print(players[i])
    value = 0
    for c in players[i]:
        value += c.golfValue()
    print(value)

print(playerNames[random.randint(0,len(playerNames)-1)] + " Wins!")
    

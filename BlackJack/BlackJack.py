from Card import Card
from Deck import Deck


def handValue(hand):
    hasAce = False
    value = 0
    for card in hand:
        if(card.num == 1):
            hasAce = True
        value += card.value()
    if hasAce and value <= 11:
        value += 10
    return value
    

dealerHand = []
yourHand = []

deck = Deck()
deck.shuffle()

dealerHand.append(deck.draw())
yourHand.append(deck.draw())
dealerHand.append(deck.draw())
yourHand.append(deck.draw())

print(dealerHand)
print(yourHand)
print(handValue(yourHand))

running = True

while running:
    
    
    
    result = input("Hit or Stay?")
    if result == "hit":
        yourHand.append(deck.draw())
    print(dealerHand)
    print(yourHand)
    print(handValue(yourHand))
    if handValue(dealerHand) <= 13:
        dealerHand.append(deck.draw())
    if result == "stay":
        while handValue(dealerHand) <= 13:
            dealerHand.append(deck.draw())
        print(dealerHand)
        print(yourHand)
        print(handValue(yourHand))
        if handValue(dealerHand) >= handValue(yourHand):
            print("You Lose")
            running = False
        else:
            print("You Win")
            running = False
    if handValue(yourHand) == 21:
        running = False
        print("Blackjack!")
    if handValue(yourHand) > 21:
        print("Bust. You Lose")
        running = False
    if handValue(dealerHand) > 21:
        print("Dealer Bust. You Win.")
        running = False
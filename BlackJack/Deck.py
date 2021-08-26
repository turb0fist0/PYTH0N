from Card import Card
import random

class Deck:
    
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(13):
                c = Card(j+1,i)
                self.cards.append(c)
        
    def shuffle(self):
        newCards = []
        for i in range(52):
            newCards.append(None)
        for card in self.cards:
            slot = random.randint(0,51)
            while(newCards[slot] != None):
                slot = random.randint(0,51)
            newCards[slot] = card
        self.cards = newCards
        
    def __repr__(self):
        return str(self.cards)
    
    def draw(self):
        return self.cards.pop()
    
    def peek(self):
        return self.cards[len(self.cards)-1]
    
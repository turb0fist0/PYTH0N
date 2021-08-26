class Card:
    
    SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
    CARDNAMES = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    
    def __init__(self, num, suit):
        
        if num < 1 or num > 13:
            raise ValueError("Invalid Card Num")
        if suit < 0 or suit > 3:
            raise ValueError("Invalid Card Suit")
        
        self.suitNum = suit
        self.suitName = Card.SUITS[self.suitNum]
        
        self.num = num
        self.cardName = Card.CARDNAMES[self.num]
        
    def value(self):
        if self.num > 10:
            return 10
        else:
            return self.num
    
    def golfValue(self):
        if self.num < 10: return self.num
        elif self.num < 13: return 10
        else: return 0
            
    def __repr__(self):
        return self.cardName + " of " + self.suitName
    
from random import choice

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ["spades", "diamonds", "clubs", "hearts"]
    
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        
    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, position):
        return self.cards[position]
    
deck = Deck()
print(f"Uses dunder len method: {len(deck)}")

print(f"We can access elements via indexing using __getitem__: {deck[0]}, {deck[1]}")

# We can only use choice if the object being passed to it is subscriptable (accessed using square bracket notation)
print(f"We can also print random items uses random.choice: {choice(deck)}")

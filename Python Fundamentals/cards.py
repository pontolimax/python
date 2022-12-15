'''2.4: Playing cards'''
import random
# Select 5 random cards from a deck of playing cards.

suits: list[str] = ['\u2663', '\u2666', '\u2665', '\u2660']
ranks: list[str] = '2,3,4,5,6,7,8,9,10,J,Q,K,A'.split(',')
cards: list[str] = [r + s for r in ranks for s in suits]
random.shuffle(cards)
hand: list[str] = [cards.pop() for _ in range(5)]
print(' '.join(hand))

# Output:
# > python .\cards.py
# 6♣ 4♥ 6♠ K♠ J♥

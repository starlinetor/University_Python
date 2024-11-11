import random

piles : list[int] = []

n_piles = random.randint(1,45)
cards_left=45

for i in range(n_piles):
    if(int((n_piles-i)/cards_left) == 1):
        pile_cards = 1
    else:
        pile_cards = random.randint(1,int(cards_left/(n_piles-i)))
    cards_left -= pile_cards
    piles.append(pile_cards)
    
piles[len(piles)-1] += cards_left    
piles.sort()
print(piles)

while piles != [1,2,3,4,5,6,7,8,9] : 

    removed_piles = []
    n_piles = len(piles)
    
    for i in range(n_piles):
        piles[i] -= 1
        if piles[i] == 0 :
            removed_piles.append(i)
    
    for i in removed_piles:
        piles.pop(i-removed_piles.index(i))
    
    piles.append(n_piles)
            
    piles.sort()
    
    print(piles)
        
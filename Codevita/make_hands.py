from collections import deque

def get_val(v):
    if v == 'A':
        return 1
    if v == 'J':
        return 11
    if v == 'Q':
        return 12
    if v == 'K':
        return 13
    return int(v)

n = int(input())

d1_init = []
d2_init = []

for _ in range(n):
    c1, s1, c2, s2 = input().split()
    v1 = get_val(c1)
    v2 = get_val(c2)
    d1_init.append((v1, int(s1)))
    d2_init.append((v2, int(s2)))

p_order = [int(x) for x in input().split()]

p_map = {}
for i in range(len(p_order)):
    s = p_order[i]
    p_map[s] = i

def key_func(card):
    v = card[0]
    s = card[1]
    p_val = 3 - p_map[s]
    return (v, p_val)

d1_init.sort(key=key_func)
d2_init.sort(key=key_func)

d1 = deque(d1_init)
d2 = deque(d2_init)

hand = []
turn = 1 

while True:
    
    deck = None
    if turn == 1:
        if not d1:
            break
        deck = d1
    else:
        if not d2:
            break
        deck = d2

    card = deck.popleft()
    
    won = False
    
    if hand:
        top = hand[-1] 
        
        if card[0] == top[0]:
            card_p = p_map[card[1]]
            top_p = p_map[top[1]]
            
            if card_p < top_p:
                won = True

    if won:
        loot = hand + [card]
        hand = [] 
        
        loot.sort(key=key_func)
        
        deck.extend(loot)
        
    else:
        hand.append(card)
        
        if turn == 1:
            turn = 2
        else:
            turn = 1

if len(d1) > 0 and len(d2) == 0:
    print("WINNER")
elif len(d1) == 0 and len(d2) > 0:
    print("LOSER")
else:
    print("TIE")
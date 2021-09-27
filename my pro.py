import random

def game(comp, b):
    if comp== b:
        return None
    elif comp == 's':
        if b =='w':
            return False
        elif b=='g':
            return True
    elif comp == 'w':
        if b =='g':
            return False
        elif b=='s':
            return True     
    elif comp == 'g':
        if b =='s':
            return False
        elif b=='w':
            return True           




print("comp's turn: Snake(s) water(w) pr Gun(g)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'    
elif randNo == 3:
    comp = 'g'     

b = input("Player's turn: Snake(s) water(w) pr Gun(g)?")

a=game(comp, b)

print(f"comp {comp}")
print(f"you {b}")
if a ==None:
    print("tie")
elif a:
    print("win")
else:
    print("lose")
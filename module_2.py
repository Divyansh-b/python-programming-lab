import random
def comp1():
    a = random.randint(2,3)
    return a

def comp2():
    a = random.randrange(1,4,2)
    return a

def comp3():
    a = random.randint(1,2)
    return a

def choice(a):
    if a==1:
        b= "Stone"
    elif a==2:
        b= "Paper"
    else:
        b="Scissor"
    return b

def win(p, q):
    if (p==1 and q==2) or (p==2 and q==3) or (p==3 and q==1):
        w = "wq"
    else:
        w = "wp"
    return w
print("\nTHE STONE PAPER SCISSOR GAME\n\nLET's START THE GAME")
a = int(input(f"\n1.Stone\n2.Paper\n3.Scissor\nEnter Your Choice (1/2/3)\n"))

if a ==1:
    xy = comp1()
elif a==2:
    xy = comp2()
elif a==3:
    xy = comp3()
else:
    print("\nWrong Value Entered !!\n")
    exit()

b = xy

c = choice(a)
d = choice(b)

if 0<a<=3:
    ans = win(a, b)
else:
    print("Wrong Value Entered")
    exit()

print(f"YOUR CHOICE = {c}")
print(f"COMPUTER's CHOICE = {d}")
if ans == "wp":
    print(f"\nYOU WIN !!\n")
else:
    print(f"\nCOMPUTER WIN\nYOU LOSE !!\n\nBETTER LUCK NEXT TIME\n")

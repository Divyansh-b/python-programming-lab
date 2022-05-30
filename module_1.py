import random

def comp():
    a = random.randint(1,6)
    return a
def check(x):
    if x%2==0:
        p = 2
    else:
        p = 1
    return p

print("PLAY THE ODD/EVEN GAME WITH THE COMPUTER\n")
print("\nLET'S START THE GAME")
a = int(input("\n1. ODD\n2. EVEN\n\nWhat do you wanna choose ? (1/2)\n"))
x = int(input("\nEnter A Number\n"))

y = comp()
print(f'\nYour Number = {x}')
print(f"Computer's Number = {y}\n")

d = x+y
n = check(d)

if n==a:
    print("\nYOU WIN !!\n")
else:
    print("\nCOMPUTER WON\nYOU LOSE !!\n\nBetter Luck Next Time")

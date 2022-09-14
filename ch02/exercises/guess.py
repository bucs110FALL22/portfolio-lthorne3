import random

rando = random.randint(0, 9)

for i in range(3):
    guesser = int(input("Guess a number 1-10: "))
    if guesser > rando:
        print("Too high")
    elif guesser < rando:
        print("Too low")
    elif guesser == rando:
        print("correct!")
        break
print("Answer is: ", rando)

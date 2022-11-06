from random import randint
import time

minLimit = 0
maxLimit = 0
value = 0

while True:
    try:
        minLimit = int(input("Select the floor: "))
        maxLimit = int(input("Select the ceiling: "))
        if minLimit < maxLimit:
            value = randint(minLimit, maxLimit)
            print()
            print("The random number is:", value)
            time.sleep(1)
            print("Bye...")
            time.sleep(1)
            break
        else:
            print("The floor must be bigger than the ceiling. Dumbass. ")
    except ValueError:
        print()
        print("Type a valid number")
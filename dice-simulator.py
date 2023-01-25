import time
import random

random.seed(time.time())
choice = 'y'

while choice == 'y':
    print("\nRolling the dice...")
    time.sleep(random.randrange(1,3))

    n = random.randrange(1,7)
    print("The dice rolled:", n)

    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Do you want to continue(y/n)? ")

import random

welcome_banner = """
                Welcome to Guess The Number!

    In this game you will have to guess a number. Good luck! 
"""

playing = True
times_done = 0

print(welcome_banner)

def guess_the_number(times_done):
    while playing:
        random_number = random.randint(1, 10)
        guess = int(input("Guess a number between 1 and 10: "))
        print(f"The random number is {random_number}.")

        difference = guess - random_number

        if guess == random_number or 0 <= difference <= 2:
            print(f"That's correct! You win $100! It took you {times_done} rounds.")
            return True
        else:
            print("Not even close! Try again.")
            times_done += 1
    return False

while not guess_the_number(times_done):
    pass

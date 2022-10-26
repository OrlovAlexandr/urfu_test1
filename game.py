'''Guess number - the game'''

import numpy as np

number = np.random.randint(1, 101) # random number

# number of attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess number from 1 to 100: "))
    
    if predict_number > number:
        print(f"The number is less than {predict_number}")
    elif predict_number < number:
        print(f"The number is greater than {predict_number}")
    else:
        print(f"You've guessed the number! It's - {number}. The number of attempts is {count}")
        break # The end of the game
        
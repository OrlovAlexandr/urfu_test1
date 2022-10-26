'''Guess the number. Computer version'''

import numpy as np

def random_predict(number:int=1) -> int:
    """ Guesses the number randomly

    Args:
        number (int, optional): hidden number, by default 1

    Returns:
        int: attempts count
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return(count)

max_num = 100

def logic_predict(number:int=1) -> int:
    """ Guesses the number logically by getting answer greater or less.

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: attempts count
    """
    count = 0
    greater = max_num
    less = 0
    attempt = greater/2
    while True:
        count += 1
        if number > attempt:
            less = attempt
            attempt = int(round((greater + less)/2))
            # print('next attempt:', attempt)
        elif number < attempt:
            greater = attempt
            attempt = int(round((greater + less)/2))
            # print('next attempt:', attempt)
        else:
            # print("bingo!", count)
            break
    return count

# logic_predict(50)

def score_game(random_predict) -> int:
    """average number of attempts for 1000 times for our algorythm

    Parameters
    ----------
    random_predict : _type_
        guessing function

    Returns
    -------
    int
        average attempts count
    """
    count_ls = []
    np.random.seed(1) # fixes seed
    random_array = np.random.randint(1, max_num+1, size=(max_num*10))
    
    for number in random_array:
        count_ls.append(logic_predict(number))
        # count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Your algorythm guesses hidden number for: {score} attempts in average')
    return(score)

score_game(random_predict)
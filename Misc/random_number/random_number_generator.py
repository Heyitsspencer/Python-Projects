import random

# Generates random number and saves it inside a variable
ran_num = random.randint(0,100)
# Defines a counter
counter = 0
while True:
    # Takes input from user
    user_input = input('Guess a number between 0 and 100!\n')
    # Turns user_input into an integer, so that it's the same value type as ran_num
    user_input = int(user_input)
    # Increments the counter up by one
    counter = counter + 1


    if user_input < ran_num:
        # Tells the user that their number is too low
        print('Your number is too low. Try again!')
        # 

    elif user_input > ran_num:
        # Tells the user that their number is too high
        print('Your number is too high. Try again!')

    else:
        # Tells the user that their number is correct
        print('Congratulations, you guessed the number correctly!')
        if counter < 5:
            # Rewards the player with 5 gold stars
            print("You did amazing, winning 5 gold stars!")
        elif counter > 5 and  counter < 10:
            # Rewards the player with 3 gold stars
            print("You did good, winning 3 gold stars!")
        elif counter > 9:
            # Rewards the player with 0 gold stars
            print("You did badly, winning 0 gold stars.")
        # Converts counter to str so it can be concatenated with a string
        counter = str(counter)
        # Tells the user how many guesses they made
        print("You made " + counter + " guess(es)")
        
        break
    


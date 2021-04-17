# While loop practice - feel free to fix any errors/make improvements in coding/explanations...
# Youtube - Programming with Mosh - Python Tutorial - Python for Beginners [Full Course]
# Building a Guessing Game - 1:24:13 - 1:31:00

# Step 1 - initial message to player...
# "\n" for a new line so it looks better:
print("\nI'm thinking of a number between 0 and 10...You get 3 tries.")
# Step 2 - establish needed variables...
# number the player should be trying to guess:
random_number = 5
# number of times the player can guess before the game ends:
number_guesses_allowed = 3
# start the count at 0, will add 1 for every player guess:
number_guess_count = 0
# Step 3 - "while" determines conditions that allow loop to continue - game length...
# "while" condition is that they have not yet guessed 3 times:
while number_guess_count < number_guesses_allowed:
    # Prints "Guess: ", allows player to input response, assigns the player's guess to "number_guess",
    # identifies input as int not string, etc.:
    number_guess = int(input("Guess: "))
    # Adds 1 to the guess count every time the player guesses, preventing infinite loop:
    number_guess_count += 1
    # Step 4 - "if" determines winning conditions...
    # "if" condition makes sure the loop will end if the player guesses correctly:
    if number_guess == random_number:
        # prints message to indicate guess was correct:
        print('You guessed it!')
        # ends game, prevents while loop from starting again after an early correct guess:
        break
# Step 5 - "else" for when "while" condition is false
# else condition for if the player uses up all their guesses without correct guess:
else:
    print('Sorry, no more tries...')

print("\nYou have 4 tries!")
# Now they are guessing a string rather than an int
favorite_color = "Orange"
color_number_guesses = 4
color_guess_count = 0
while color_guess_count < color_number_guesses:
    color_guess = input("Guess my favorite color: ")
    # update to change message for subsequent inputs ("Guess again: ")? Simplest way?
    color_guess_count += 1
    # using .title to reformat player input to match "Orange" - so they can say orange or ORANGE - still matches.
    if color_guess.title() == favorite_color:
        # could have done .lower() or .upper() by changing "favorite_color =" to orange or ORANGE - personal preference.
        print("That's correct!")
        break
else:
    print("Game over.")

# identical to guessing color:
print("\nYou have 3 tries!")
favorite_day = "Monday"
day_number_guesses = 3
day_guess_count = 0
while day_guess_count < day_number_guesses:
    day_guess = input("Guess my favorite day of the week: ")
    # update to change message for subsequent inputs? Simplest way?
    day_guess_count += 1
    if day_guess.title() == favorite_day:
        print("Correct!")
        break
else:
    print("Sorry, no more chances...")

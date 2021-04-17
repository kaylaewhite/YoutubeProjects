# The Car Game - feel free to fix any errors/make improvements in coding/explanations...
# Youtube - Programming with Mosh - Python Tutorial - Python for Beginners [Full Course]
# Building the Car Game - 1:30:57 - 1:41:54

command = ""
# empty quotes for command to allow use of player input
started = False
# establishes that the car is stopped, allows for this condition to change...
# ...thus a stopped car can't be stopped twice in a row, a started car can't be started twice.
while True:
    # "True" enables the while loop to keep running until "break"
    command = input("> ").lower()
    # assigns player input to command, makes it all lowercase
    if command == "start":
        if started:
            print("The car was already started!")
            # If player enters start when car is already started, they get above message.
        else:
            started = True
            print("The car has started.")
            # If player enters start when car is stopped, they get this message, started condition changes to True
    elif command == "stop":
        if not started:
            print("The car was already stopped!")
            # Prevents player from stopping a stopped car
        else:
            started = False
            print("The car has stopped.")
            # Stops the car which was started, changes started condition to False
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to end the program
        """)
        # prints help guide for player in multiline string
    elif command == "quit":
        break
        # ends loop
    else:
        print("Sorry, I don't understand.")
        # if player enters any unknown command, they see this

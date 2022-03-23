import random
from urllib import response


# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # interates through list and if response is an item
        # in the list (or the first letter of an item), the full item 
        # name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


# Main routine goes here

# Lists of valid responses 
yes_no_list = ["yes", "no"]
rps_list = ["paper", "scissors", "rock", "xxx"]

# Ask user if they have played before.
# If 'yes', show instructions


# ask user for # of rounds then loop...
game_summary = []

rounds_played = 0

# intialise lost / drawn counters
rounds_lost = 0
rounds_drawn = 0

# Ask  user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Rounds {} (xxx to quit)".format(rounds_played + 1)
    else:
        heading = "Rounds {} of {}".format(rounds_played +1, rounds)

    print(heading)
    choose_instruction = "Please choose paper (p), scissors (s), or rock (r) "
    choose_error = "Please choose from paper / scissors / rock (or xxx to quit)"

    # Ask user for choice and check it's valid
    user_choice = choice_checker(choose_instruction, rps_list, choose_error)
    

    # End game if exit code is typed
    if user_choice == "xxx":
        print("***** Thanks for playing *****")
        break

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # compare choices
    if comp_choice == user_choice:
        result = "tie"
        rounds_drawn += 1
    elif user_choice == "rock" and comp_choice == "scissors":
        result = "won"
    elif user_choice == "papper" and comp_choice == "rock":
        result = "won"
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        feedback = "It's a tie"
    else:
        feedback = "{} vs {} - you {}".format(user_choice, comp_choice, result)    

    # **** rest of loop / game *****
    print("You chose {} vs {} - {}".format(user_choice, comp_choice, result))

    rounds_played += 1


    # Ask user if they want to see their game history.
    if user_choice.lower == "xxx" or rounds_played == rounds:
        break

print()
user_history = input("Would you like to see your game history? ").lower()
if user_history == "yes" or user_history == "y":
    user_history = "yes" 
    
    rounds_won = rounds_played - rounds_lost - rounds_drawn


# If 'yes' show game history


# Show game statistics
# **** Calculate Game Stats ******
    percent_win = (rounds_won / rounds_played) * 100
    percent_lose = (rounds_lost / rounds_played) * 100
    percent_tie = (rounds_drawn / rounds_played) * 100

    print()
    print("***** Game History *******")
    for game in game_summary:
        print(game)

    print()

    # displays game stats with % values to the nearest whole number
    print("******* Game Statistics *******")
    print("Win: {}, ({:.0f}%) ".format(rounds_won, percent_win))
    print("Loss: {}, ({:.0f}%) ".format(rounds_lost, percent_lose))
    print("Tie: {}, ({:.0f}%) ".format(rounds_drawn, percent_tie))
            

    # End of Game Statements 
    print()
    print('***** End Game Summary *****')
    print("Won: {} \t|\t List:{} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))

print()
print("***** Thanks for playing *****")


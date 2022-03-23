# Functions used to check input is valid


def check_rounds():
    while True:
        reponse = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0"
        if reponse != "":
            try:
                response = int(reponse)

                if reponse < 1 :
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response



# Main routine goes here...

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p) pr scissors (s)"

# Ask  user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Rounds {}".format(rounds_played + 1)
        print(heading)
        choose = input("{} or 'xxx' to end: ".format(choose_instruction))
        if choose == "xxx":
            break
    else:
        heading = "Rounds {} of {}".format(rounds_played +1, rounds)
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds - 1:
            end_game = "yes"


    # rest of loop / game
    print("You chose {}".format(choose))

    rounds_played += 1

print("Thank you for playing")
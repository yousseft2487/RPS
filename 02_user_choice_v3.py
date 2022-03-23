# Version 3 - checks that reponse is in a given list


# Functions go here
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


# lists for checking reponses
rps_list = ["rock", "paper", "scissors", "xxx"]

# Loop for testing purposes 
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    user_choice = choice_checker("Choose paper / scissors / rock (r/p/s): ", rps_list,
                                 "Please choose from paper / scissors / rock / "  
                                 "(or xxx to quit)")

    # print out choice for comparison purposes 
    print("You chose {}".format(user_choice))  

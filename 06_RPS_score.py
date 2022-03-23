# RPS Component 6 - Scoring System

# Rounds won will be calculated (total - draw - lost)
rounds_played = 0
rounds_lost = 0
rounds_drawn = 0

# Results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# Play Game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item
    
    if result == "tie":
        reult = "It's a tie"
        rounds_drawn += 1
    elif result == "loss":
        rounds_lost += 1

# Quick calculations (status)
rounds_won = rounds_played - rounds_lost - rounds_drawn

# End of Game Statements 
print()
print('***** End Game Summary *****')
print("Won: {} \t|\t List:{} \t|\t Draw: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print(" Thanks for playing")
# RPS Component 1 - generate computer choice

import random

rps_list = ["paper", "scissors", "rock"]

for item in range(0,20):
    comp_choice = random.choice(rps_list)
    print(comp_choice, end="/t")
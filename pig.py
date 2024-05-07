"""
games of rolling a dice with turns etc..

"""
import random

def roll():
    roll_dice = random.randint(1,6)
    return roll_dice

set_players = False
while not set_players:
    try:
        players = int(input("Enter the number of players (2-4): "))
        if 2 <= players <=4:
            set_players = True
        else:
            print("Please only select between 2 to 4")
    except ValueError:
        print("Please type only numbers")


max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores)< max_score:
    
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx+1}, your turn has just started!\n")
        print(f"Your Total Score is: {player_scores[player_idx]}\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != 'y':
                break

            dice_value = roll()
            if dice_value == 1:
                print("You rolled a 1 ! Turn done!")
                current_score = 0
                break
            else:
                current_score+=dice_value
                print(f"You rolled a: {dice_value}")

            print(f"You're score is: {current_score}")
        player_scores[player_idx]+= current_score
        print(f"Your Total Score is: {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
final_msg =f"The Player number {winning_idx + 1} is the wiiner with a score of: {max_score}!" 
print("*"*len(final_msg))
print(final_msg)
print("*"*len(final_msg))
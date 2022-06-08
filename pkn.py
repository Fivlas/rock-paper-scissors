import random

user_wins = 0
bot_wins = 0
game_draw = 0

options = ["rock", "paper", "scissors"]
options[0]
while True:
    user_input = input("Type Rock/Papier/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        print("Invalid input")
        continue
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2 
    bot_pick = options[random_number]
    print("Bot picked", bot_pick + ".")
    
    if user_input == "rock" and bot_pick == "scissors":
        print("You Won!")
        user_wins += 1
    
    elif user_input == "paper" and bot_pick == "rock":
        print("You Won!")
        user_wins += 1
    
    elif user_input == "scissors" and bot_pick == "paper":
        print("You Won!")
        user_wins += 1
    
    elif user_input == bot_pick:
        print("Draw!")
        game_draw += 1
        
    else:
        print("You Lost!")
        bot_wins += 1
        
print("You won", user_wins, "times.")
print("The bot won", bot_wins, "times." )
print("Draw was", game_draw, "times.")
print("Goodbye!")
import random

opcje = ["papier", "kamien", "nozyce"]
random1 = random.randint(0,2)
bot = opcje[random1]
user_wins = 0
bot_wins = 0
game_draw = 0

while True:
    player_pick = input("Wybierz Papier/Kamien/Nozyce lub quit by wyjsc lub wyniki by sprawdzic wyniki\n").lower()

    if player_pick == "quit":
        cos = input("jestes pewny Y/n\n").lower()
        if(cos == "y"):
            break
        else:
            continue

    if player_pick == "wyniki":
        print("\nWygrales:", user_wins, "\nBot wygrał:", bot_wins, "\nRemis:", game_draw)
        continue


    if player_pick not in opcje and not "wyniki":
        print("\nNie ma takiego ruchu")
        continue

    print("\nBot wybral", bot + ".")

    if player_pick == "kamien" and bot == "nozyce":
        print("Wygrales!\n")
        user_wins += 1
    
    elif player_pick == "papier" and bot == "kamien":
        print("Wygrales!\n")
        user_wins += 1
    
    elif player_pick == "nozyce" and bot == "papier":
        print("Wygrales!\n")
        user_wins += 1
    
    elif player_pick == bot:
        print("Remis!\n")
        game_draw += 1
        
    else:
        print("Przegrales!\n")
        bot_wins += 1

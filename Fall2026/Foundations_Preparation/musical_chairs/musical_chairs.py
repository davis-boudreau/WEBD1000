# Author: Davis Boudreau
# Student ID: w0305171
# Course: PROG 1700
# Date: November 11, 2026
# Version: 0.1

# Modules
import random

# 1. Initialize variables and lists
players = []
eliminated_players = []
num_players = 0
rounds = 1

# Game Greeting
print("Welcome to Musical Chairs")
print("_________________________")

while True:
    try:
        num_players = int(input("Number of players: "))
        if num_players >= 2:
            break
        else:
            print("Error: Enter a valid number (Musical Chairs requires at least 2 players)")
    except ValueError:
        print("Error:  Enter a valid whole number")

while len(players) < num_players:
    player_name = input("Enter player name: ").strip()
    if player_name == "":
        print("Error: Name cannot be blank")
    elif player_name in players:
        print("Error: Player already registered.")
    else:
        players.append(player_name)
        print(f"{player_name} successfully registered.")
        
print("\nGame Starting")
print("One player will be eliminated each round.")
print("The last remaining player wins.")

while len(players) > 1:
    chairs = len(players) - 1
    print("\n----------------------")
    print(f"Round: {rounds}")
    print(f"Number of Players: {len(players)}")
    print(f"Number of Chairs: {chairs}")
    print("\nActive Players:")
    for p in players:
        print(p)

    input("\nMusic playing......Press Enter to stop.")
    
    # Randomly select a player
    eliminated = random.choice(players)

    # Remove the player and record elimination
    players.remove(eliminated)
    eliminated_players.append(eliminated)

    print(f"\n{eliminated} has been eliminated")
    print(f"Remaining players: {len(players)}")

    rounds += 1

# Display final results
print("\n=================================")
print("Game Over")
print("\n=================================")

print(f"Winner: {players[0]}")
print(f"Rounds Played: {rounds - 1}")













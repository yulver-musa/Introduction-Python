def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    player = input("Multiplayer or Single-player? ")
    if not (player == "Multiplayer" or difficulty == "Single-player"):
        print("Enter a valid number of players")
        return

    if difficulty == "Difficult" and player == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and player == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and player == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

def recommend(game):
    print("You might like", game)


main()

def main():
    difficulty = input("Difficult or Casual? ")
    player = input("Multiplayer or Single-player? ")

    if difficulty == "Difficult":
        if player == "Multiplayer":
            recommend("Poker")
        elif player == "Single-player":
            recommend("Klondike")
        else:
            print("Enter a valid number of players")
    elif difficulty == "Casual":
        if player == "Multiplayer":
            recommend("Hearts")
        elif player == "Single-player":
            recommend("Clock")
        else:
            print("Enter a valid number of players")
    else:
        print("Enter a valid difficulty")

def recommend(game):
    print("You might like", game)


main()

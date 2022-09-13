import random


def get_choices():
    question = True
    while (question):
        player_choice = input("Enter a choice (rock, paper, scissors): ")
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        if (player_choice == "rock" or player_choice == "paper" or player_choice == "scissors"):
            question = False
        else:
            print("You should enter either rock, paper or scissors")
        choices = {
            "player": player_choice,
            "computer": computer_choice
        }
        return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! You win!"


# choices = get_choices()
# print(choices)

import random


def get_choices():
    options = ["rock", "paper", "scissors"]
    player_choice = input("enter a choice (rock, paper or scissors): ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices


def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}")
    if player == computer:
        return "result was a draw"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers Rock. You Lose!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors! You lose!"
        else:
            return "scissors cut paper You Win!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock. You Win!"
        else:
            return "scissors cut paper You Lose!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

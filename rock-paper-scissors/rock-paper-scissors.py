from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import random

# main window
root = Tk()
root.configure(background="white")

# Load the images
rock_image = tk.PhotoImage(file="images/rock-emoji.png")
paper_image = tk.PhotoImage(file="images/paper-emoji.png")
scissors_image = tk.PhotoImage(file="images/scissors-emoji.png")

# Create placeholder labels for player and computer moves
player_move_label = tk.Label(root, image=scissors_image, background="white")
player_move_label.grid(row=0, column=0)

computer_move_label = tk.Label(root, image=scissors_image, background="white")
computer_move_label.grid(row=0, column=2)

# Create a dictionary to store the possible outcomes
outcomes = {
    ("rock", "rock"): "Tie",
    ("rock", "paper"): "You lose",
    ("rock", "scissors"): "You win",
    ("paper", "paper"): "Tie",
    ("paper", "scissors"): "You lose",
    ("paper", "rock"): "You win",
    ("scissors", "scissors"): "Tie",
    ("scissors", "rock"): "You lose",
    ("scissors", "paper"): "You win"
}

# Create StringVar variables to update the labels automatically
result_var = tk.StringVar()
moves_var = tk.StringVar()
score_var = tk.StringVar()

# Initialize interval_id as a global variable
interval_id = None

def play_game(player_move):
    computer_move = random.choice(["rock", "paper", "scissors"])

    # Update the images for player and computer moves
    player_move_label.config(image=get_image(player_move), background="white")
    computer_move_label.config(image=get_image(computer_move), background="white")

    # Get the outcome from the dictionary
    result = outcomes[(player_move, computer_move)]

    update_score(result)

    # Update the result variable
    result_var.set(result)

    # Update the moves variable
    moves_var.set(f"You: {player_move} vs. Computer: {computer_move}")

    # Update the score variable
    score_var.set(f"Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")

def update_score(result):
    if result == "You win":
        score["wins"] += 1
    elif result == "You lose":
        score["losses"] += 1
    else:
        score["ties"] += 1

def get_image(move):
    if move == "rock":
        return rock_image
    elif move == "paper":
        return paper_image
    else:
        return scissors_image
#
# def auto_play():
#     global interval_id
#     # Get the current text of the button
#     current_text = auto_play_button["text"]
#
#     if current_text == "Auto Play":
#         # Change the text and command of the button
#         auto_play_button.config(text="Stop Auto Play", command=stop_auto_play)
#
#         # Schedule the autoplay function to run every second
#         interval_id = root.after(1000, lambda: play_game(random.choice(["rock", "paper", "scissors"])))
#     else:
#         # Change the text and command of the button
#         auto_play_button.config(text="Auto Play", command=auto_play)
#
#         # Cancel the scheduled autoplay function
#         root.after_cancel(interval_id)

# def stop_auto_play():
#     # Call the auto_play function again
#     auto_play()

def reset_score():
    score["wins"] = 0
    score["losses"] = 0
    score["ties"] = 0

    # Reset the result variable
    result_var.set("")

    # Reset the moves variable
    moves_var.set("")

    # Reset the score variable
    score_var.set(f"Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}")

score = {"wins": 0, "losses": 0, "ties": 0,}

root.title("Rock Paper Scissors")

rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"), background="white")
rock_button.grid(row=1, column=0)

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"), background="white")
paper_button.grid(row=1, column=1)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"), background="white")
scissors_button.grid(row=1, column=2)

# auto_play_button = tk.Button(root, text="Auto Play", command=auto_play, background="white")
# auto_play_button.grid(row=2, column=0)

reset_score_button = tk.Button(root, text="Reset Score", command=reset_score, background="white")
reset_score_button.grid(row=2, column=1)

# Assign the StringVar variables to the labels
result_label = tk.Label(root, textvariable=result_var, background="white")
result_label.grid(row=3, column=0, columnspan=3)

moves_label = tk.Label(root, textvariable=moves_var, background="white")
moves_label.grid(row=4, column=0, columnspan=3)

score_label = tk.Label(root, textvariable=score_var, background="white")
score_label.grid(row=5, column=0, columnspan=3)

root.mainloop()

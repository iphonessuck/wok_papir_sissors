import random

choices = ["rock", "paper", "scissors"]
print("rock, paper, scissors")
robot_choice = random.choice(choices)
choice = input("")
print(robot_choice)

if robot_choice == "rock":
    if choice == "paper":
        print("you win")
        print("you beat a robot are you happy with yourself")
if robot_choice == "paper":
    if choice == "rock":
        print("you lost")
        print("you lost to a robot LMAO")
if robot_choice == "rock":
    if choice == "rock":
        print("tie ")
        print("you are as smart as a tin can idiot")
if robot_choice == "rock":
    if choice == "scissors":
        print("you lost")
        print("you are so pathetic")
if robot_choice == "paper":
    if choice == "scissors":
        print("you win")
        print("do you get some kind of sick joy from this?")
if robot_choice == "paper":
    if choice == "paper":
        print("you tied")
        print("even chatGPT can predict you have 3.2 IQ")
if robot_choice == "scissors":
    if choice == "paper":
        print("you are a loser")
        print("when you play fortnite everyone L dances on you")
if robot_choice == "scissors":
    if choice == "scissors":
        print("you tie with a tin can")
        print("you suck at life, go be sober or smth")
if robot_choice == "scissors":
    if choice == "rock":
        print("you won")
        print("does this make you fell better about yourself?")
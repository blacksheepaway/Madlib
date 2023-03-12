def RPS():
    # ascii art for the hands
    rock_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

    paper_art = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

    scissors_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

    # Dictionary of the hand choices
    hands = {"rock": rock_art, "paper": paper_art, "scissors": scissors_art}

    # user input
    userinput = input("Enter your choice (rock, paper, or scissors): ")
    
    # check if user input is valid
    if userinput not in hands:
        print("Invalid input!")
        return

    # computer choice
    import random
    computerinput = random.choice(list(hands.keys()))

    # user and computer choices
    print(f"You chose {userinput}:\n{hands[userinput]}")
    print(f"Computer chose {computerinput}:\n{hands[computerinput]}")

    # determining winner
    if userinput == computerinput:
        print("It's a tie!")
    elif userinput == "rock":
        if computerinput == "paper":
            print("You lost!")
        else:
            print("You won!")
    elif userinput == "paper":
        if computerinput == "scissors":
            print("You lost!")
        else:
            print("You won!")
    elif userinput == "scissors":
        if computerinput == "rock":
            print("You lost!")
        else:
            print("You won!")

RPS();
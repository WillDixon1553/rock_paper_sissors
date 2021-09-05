while 1:
    choice = input("Rock, paper or scissors?: ").lower()
    if choice == "rock":
        print("Haha I went paper. Get wrecked!")
    elif choice == "paper":
        print("I went scissors. I guess I win!")
    elif choice == "scissors":
        print("I chose rock so yeah. Sucks to suck!")
    else:
        print("Not a valid input!")

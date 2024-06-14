import random
choices = ["rock","paper","scissors"]
player =  None
bot_choice = random.choices

while player not in choices:
    player = input("rock, paper, scissors? : ").lower() 
    print ("Invalid choice! Please enter rock, paper or scissors.")
    player = input("Enter again: ")
    if bot_choice == player:
        print("Its a tie")
    elif player=="paper":
        if bot_choice== "rock":
         print("Player: ",player)
         print("Computer: ",bot_choice)
         print("You Win")
        if bot_choice== "scissors":
         print("Player: ",player)
         print("Computer: ",bot_choice)
         print("You Win")
    elif player=="rock":
        print("I Win because I chose paper and you chose rock")
    elif player=="paper":
        print("I Win")
    elif player=="scissors":
        print("You Win")
    else:
        print("Lets Play again")
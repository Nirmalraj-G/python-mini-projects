import random

user = 0
computer = 0

options = ["stone", "paper", "scissor"]

while True:
    user_type = input("Type stone/paper/scissor or Exit: ").lower()
    
    if user_type == "exit":
        quit()
    
    if user_type not in options:
        print("Type only from the option")
        continue
    
    random_number = random.randint(0,2)
    
    computer_type = options[random_number]
    
    print("computer: ",computer_type)
    
    if user_type == "stone" and computer_type == "paper":
        print("you lost!")
        computer+=1
    elif user_type == "stone" and computer_type == "scissor":
        print("you won!")
        user+=1
    elif user_type == "stone" and computer_type == "stone":
        print("Draw!")
    elif user_type == "paper" and computer_type == "stone":
        print("you won!")
        user+=1
    elif user_type == "paper" and computer_type == "scissor":
        print("you lost!")
        computer+=1
    elif user_type == "paper" and computer_type == "paper":
        print("Draw!")
    elif user_type == "scissor" and computer_type == "stone":
        print("you lost!")
        computer+=1
    elif user_type == "scissor" and computer_type == "paper":
        print("you won!")
        user+=1
    else:
        print("Draw!")
    
    
    print("Your score: ",user)
    print("computer score: ",computer)

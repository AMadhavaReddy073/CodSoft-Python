import random
# Rules for the game
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Please enter your choice: \n 1)Rock \n 2)Paper \n 3)Scissor ")

    user_action = int(input("select an action 1/2/3 : "))

    while user_action > 3 or user_action < 1 :
         user_action = int(input("Enter a valid action: ")) 

   
    #user choice
    if user_action == 1:
        choice_name = 'Rock'
    elif user_action == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print ("Your Choice is : ", choice_name)


    computer_choice = random.randint(1,3)

    while computer_choice == user_action:
        computer_choice = random.randint(1, 3)

    #computer's choice
    if computer_choice == 1:
        comp_choice_name = 'RocK'
    elif computer_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer's Choice is :", comp_choice_name)

    #checking for draw
    if user_action == computer_choice:
        print('Its a Draw', end="")
        result = "DRAW"

    #Condition to win
    if (user_action == 1) and (computer_choice == 2):
        print("Paper covers rock! You lose.")
    elif (user_action == 2) and (computer_choice == 1):
        print("Paper covers rock! You win!")
    
    if (user_action == 1) and (computer_choice == 3):
        print("Rock smashes scissors! You win!")
    elif (user_action == 3) and (computer_choice == 1):
        print("Rock smashes scissors! You lose.")

    if (user_action == 2) and (computer_choice == 3):
        print("Scissors cuts paper! You lose.")
    elif (user_action == 3) and (computer_choice == 2):
        print("Scissors cuts paper! You win!")

    #playing another round
    print("Do you want to play again? (Y/N)")
    
    ans = input().lower()
    if ans == 'n':
        break


#greeting at the end
print("Thank you for Playing")
        
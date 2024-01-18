#*****Rock-Paper-Scissors-Game*****
import random 
def main():
  print("Welcome to Rock-Paper-Scissors!")
  print("Enter 1 for Rock, 2 for Paper, 3 for Scissors: ")
  user_choice = int(input("Enter your choice: "))
  computer_choice = random.randint(1,3)
  print("computer choosed: ",computer_choice)
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == 1 and computer_choice == 2:
    print("Computer wins!")
  elif user_choice == 1 and computer_choice == 3:
    print("You win!")
  elif user_choice == 2 and computer_choice == 1:
    print("You win!")
  elif user_choice == 2 and computer_choice == 3:
    print("Computer wins!")
  elif user_choice == 3 and computer_choice == 1:
    print("Computer wins!")
  elif user_choice == 3 and computer_choice == 2:
    print("You win!")
  else:
    print("Invalid choice. Please try again.")
    
main()

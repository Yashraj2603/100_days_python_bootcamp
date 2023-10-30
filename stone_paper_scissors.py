import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("WELCOME TO ROCK PAPER SCISSORS")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice = int(input())
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)

if computer_choice == 0:
    print("Computer chooses Rock")
elif computer_choice == 1:
    print("Computer chooses Paper")
elif computer_choice == 2:
    print("Computer chooses Scissors")
else:
    print("Invalid choice. Please choose 0, 1 or 2.")

if choice == computer_choice:
    print("Draw ")
elif choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 0 and computer_choice == 2:
    print("You won")
elif choice == 1 and computer_choice == 0:
    print("You won")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 0:
    print("You lose")
elif choice == 2 and computer_choice == 1:
    print("You won")
else:
    print("Invalid choice. Please choose 0, 1 or 2.")

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

choices = [rock, paper, scissors]

# Game loop
while True:
    # Ask user for their choice
    user = int(input("What do you want to choose? Type 0 for rock, 1 for paper, 2 for scissors:\n"))
    computer = random.randint(0, 2)

    # Display the user's and computer's choice
    print(f"You chose:\n{choices[user]}")
    print(f"The computer threw:\n{choices[computer]}")

    # Determine the outcome
    if (user + 1) % 3 == computer:
        print("You lost!")
    elif user == computer:
        print("It's a draw!")
    else:
        print("You win!")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break

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

def selection(n):
    if n == 0:
        print(rock)
    if n == 1:
        print(paper)
    if n == 2:
        print(scissors)

def score(user, comp):
    if (user == 0 and comp == 2) or (user > comp):
        print("You win!")
    elif (comp == 0 and user == 2) or (user > comp):
        print("You lose!")
    elif (comp == user):
        print("A draw!")
    else:
        print("Invalid input entered")

def game():
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))
    comp = random.randint(0,3)

    print("\n\nUser:")
    selection(user)
    print("Computer:")
    selection(comp)

    score(user, comp)


game()

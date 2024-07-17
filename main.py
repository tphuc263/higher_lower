import os
from art import logo, vs
from game_data import data
import random

#Creat new object to compare
def new_object(list_data):
  len_list = len(list_data)
  ran_num = random.randint(0, len_list - 1)
  new_obj = list_data[ran_num]
  return new_obj
  
#Compare two object
def is_right_guess(guess, num1, num2):
  # guess is compare num2 and num1
  if (guess == 'higher'):
    if (num2 > num1):
      return True
    else:
      return False
  elif (guess == 'lower'):
    if (num2 < num1):
      return True
    else:
      return False
  else:
    return False
  
#To start a new game
def higher_lower():
  print(logo)
  print("Welcome to Higher or Lower game!! Have Fun!")
  score = 0
  obj_1 = new_object(list_data = data)
  obj_2 = new_object(list_data = data)
  is_continue = True
  while (is_continue):
    print(f"Name: {obj_1['name']}, is {obj_1['description']} from {obj_1['country']}")
    print(f"Follower of {obj_1['name']} is {obj_1['follower_count']}")
    print(vs)
    print(f"Name: {obj_2['name']}, is {obj_2['description']} from {obj_2['country']}")
    guess_of_player = input("Type your choice 'Higher' or 'Lower': ").lower()
    is_correct = is_right_guess(guess = guess_of_player, num1 = obj_1['follower_count'], num2 = obj_2['follower_count'])
    if (is_correct):
      score += 1
      obj_1 = obj_2
      obj_2 = new_object(list_data = data)
      os.system("clear")
      print(f"Correct Choice!!, current score: {score}")
    else:
      print("Wrong!!! ")
      print(f"Your final Score: {score}")
      is_continue = False

#Type "y" is you want to play game again or 'n' to exit
again = True
while again:
  higher_lower()
  choice = input("Type 'y' to continue play or 'n' to exit: ").lower()
  if (choice == 'n'):
    again = False
  elif (choice == 'y'):
    os.system("clear")

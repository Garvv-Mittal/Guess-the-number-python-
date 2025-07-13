from art import logo
import random

print(logo)# Display the logo
print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100.")
difficulty = input("choose a Difficulty. Type 'easy' or 'hard': ")

n = random.randint(1,100)# Generate a random number between 1 and 100

def game():# function to run the game
  attempts = 0
  guess = int(input("make a guess: "))
  if n > guess:
    print("Too low")
    
  elif n < guess:
    print("Too high")
    
  elif n == guess:
    print(f"You got it ! , the ansewer was {n}.")
    return True

if difficulty == "easy": # easy mode
  attempts =10
  print(f"You have {attempts} attempts remaining to guess the number.")
  while attempts >0:
    if game():
      break # if the user guesses correctly stops the loop
    attempts -= 1
    if attempts>0: 
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print(f"You've run out of guesses, you lose. the answer was {n}.")
    
elif difficulty == "hard" : # hard mode
  attempts =5
  print(f"You have {attempts} attempts remaining to guess the number.")
  while attempts >0:
    if game():
      break # if the user guesses correctly
    attempts -= 1
    if attempts>0: 
      print(f"You have {attempts} attempts remaining to guess the number.")
    else:
      print(f"You've run out of guesses, you lose. the answer was {n}.")
import random

while True:
  guess = 0
  attempts = 0
  secret_number = random.randint(1, 10)
  while True:
    guess = int(input('I ve been asked to guess a number between 1 and 10. Write the number here -->  '))
    attempts += 1
    if guess == secret_number:
        print(f'You guessed it! You did it after so many tries: {attempts}')
        break
    elif guess > secret_number:
        print('Your number is greater!')
    elif guess < secret_number:
        print('Your number is less!')
  play_again = input('Good job! Do you want to play again? (Write yes/no)')
  if play_again.lower() != 'yes':
     break 

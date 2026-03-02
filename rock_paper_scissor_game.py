import random

emojis = {'r': '🪨', 'p': '📄', 's': '✂️'}
choices = ('r', 'p', 's')

while True:
    user_choice = input('Rock, Paper, Scissor? (r/p/s): ').lower()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue 

    computer_choice = random.choice(choices)
    print(f'You choose {emojis[user_choice]}')
    print(f'Computer choose {emojis[computer_choice]}')

    if user_choice == 'r':
        if computer_choice == 'r':
            print("It's a tie!🤝")
        elif computer_choice == 'p':
            print('You lose!👎')
        else:
            print('You Win!🥳')
    elif user_choice == 'p':
        if computer_choice == 'r':
            print('You Win!🥳')
        elif computer_choice == 'p':
            print("It's a tie!🤝")
        else:
            print('You lose!👎')
    else:
        if computer_choice == 'r':
            print('You lose!👎')
        elif computer_choice == 'p':
            print('You Win!🥳')
        else:
            print("It's a tie!🤝")

    should_continue = input('Play Again? (y/n): ').lower()
    if should_continue == 'n':
        print('Thanks for Playing!')
        break



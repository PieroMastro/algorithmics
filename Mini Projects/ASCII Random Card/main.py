from random import choice, randint

suits = ['♥️', '♦️', '♠️', '♣️']
numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def get_random_card():
    # Prints an ASCII representation of a random card to the terminal
    rank = choice(numbers)
    suit = choice(suits)

    print('Your card:')
    if rank != 10:
        random_card = f"""
    ┌───────┐
    │ {rank}     │
    │   {suit}   │
    │     {rank} │
    └───────┘
    """
    else:
        random_card = f"""
    ┌───────┐
    │ 10    │
    │   {suit}   │
    │    10 │
    └───────┘
    """       
    
    print(random_card) 

def run_app():
    # Runs the card drawing application
    while True:
        user_choice = input("Do you want to pick a card? (y/n): ")
        if user_choice.lower() == 'y':
            get_random_card()
        elif user_choice.lower() == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

run_app()
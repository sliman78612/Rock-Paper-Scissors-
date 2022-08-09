import random 

def get_computer_choice():
    choices = ['Rock','Paper','Scissors']
    return random.choice(choices)

def get_user_choice():
    user_choice = input('Enter "Rock", "Paper" or "Scissors" : ')
    return user_choice

def get_winner(comp,user):
    print(f'Computer went {comp}')
    if comp=='Rock' and user == 'Scissors' or comp == 'Paper' and user == 'Rock' or comp == 'Scissors' and user == 'Paper':
        return 'Computer Wins'
    elif comp==user:
        return "It's a draw"
    else:
        return 'Congrats! You Win.'


def play():
    comp_choice = get_computer_choice()
    user_choice = get_user_choice()
    print (get_winner(comp_choice,user_choice))

#print(get_winner(get_computer_choice(),get_user_choice()))

play()
import random 

def get_user_choise () :
    while True :
        user_choise = input("Chose sign(rock, scissor, paper)").lower()
        if user_choise in ['rock', 'scissor', 'paper'] :
            return user_choise
        else :
            print('Wrong sign')

def computer_chose () :
    return random.choice(['rock', 'scissor', 'paper'])    

def find_winner(user_sign, computer_sign) :
    if user_sign == computer_sign :
        return 'No winers'
    elif (user_sign == 'rock' and computer_sign == 'scissor') or \
         (user_sign == 'scissor' and computer_sign == 'paper') or \
         (user_sign == 'paper' and computer_sign == 'rock') :
        return 'You won'
    else :
        return "You lose"


def main () :
    user_sign = get_user_choise()
    computer_sign = computer_chose()
    result = find_winner(user_sign, computer_sign)

    print(f"Your choice: {user_sign}")
    print(f"Computer's choice: {computer_sign}")
    print(result)
main()    
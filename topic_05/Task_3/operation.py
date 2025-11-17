from function import add, minus, multiply, devide

def get_num_for_user (prompt) :
    while True :
        num_input = input(prompt)
        if num_input == 'exit':
            return None
        try :
            return float(num_input)
        except ValueError:
            print('Invalid input, try input number: ')

def get_operator () :
    while True:
        operator = input('Input operator(+, -, *, /): ')
        if operator not in ['+', '-', '*', '/']:
            print('Invalid operator')
            continue
            
        else :
            return operator


def execute_number (num_1, num_2, operator) :
    match operator:
            case "+":
                print('Result is :', add(num_1, num_2))
            case "-":
                print('Result is :', minus(num_1, num_2))
            case "*":
                print('Result is :', multiply(num_1, num_2))        
            case "/":
                print('Result is :', devide(num_1, num_2))

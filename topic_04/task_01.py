def add (a, b):
    return a + b

def minus (a, b):
    return a - b

def multiply (a, b):
    return a * b

def devide (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Zero division error')

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


def main ():
    while True:
        num_1 = get_num_for_user("Enter first number or 'exit' to quit: ")
        if num_1 == None :
            print('exiting...')
            break

        num_2 = get_num_for_user("Enter second number or 'exit' to quit: ")
        if num_2 == None :
            print('exiting...')
            break
        
        operator = get_operator()

        match operator:
            case "+":
                print('Result is :', add(num_1, num_2))
            case "-":
                print('Result is :', minus(num_1, num_2))
            case "*":
                print('Result is :', multiply(num_1, num_2))        
            case "/":
                print('Result is :', devide(num_1, num_2))               

main()                
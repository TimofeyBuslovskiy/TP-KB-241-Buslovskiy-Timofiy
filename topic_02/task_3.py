def plus (a, b) :
    return a + b

def minus (a, b) :
    return a - b

def multiply (a, b) :
    return a * b

def devide (a, b) :
    return a / b

def calculator (num_1, num_2, operator) :  

    match operator :
        case '+':
            return num_1 + num_2
        case '-':
            return num_1 - num_2
        case '*':
            return num_1 * num_2
        case '/':
            return num_1 * num_2
    


num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))
operator = input('Enter your action: ')

print(calculator(num_1, num_2, operator))
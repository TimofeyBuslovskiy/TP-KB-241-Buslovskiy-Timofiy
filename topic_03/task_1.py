def plus (a, b) :
    return a + b

def minus (a, b) :
    return a - b

def multiply (a, b) :
    return a * b

def devide (a, b) :
    return a / b

def calculator () :
    while True :

        num_1_inp = input("Ведіть перше число(щоб вийти напишіть 'exit'): ")
        if num_1_inp.lower() == 'exit':
            print("Роботу калькулятора припинено")
            break

        try :
            num_1 = float(num_1_inp)
        except ValueError:
            print('Несправильно введене число, спробуйте ще раз')
            continue

        num_2_inp = input('Введіть друге число:')

        try :
            num_2 = float(num_2_inp)
        except ValueError:
            print('Несправильно введене число, спробуйте ще раз')
            continue

        operator = input("Введіть оператор: ")

        match operator :
            case '+':
                print(plus(num_1, num_2))
            case '-':
                print(minus(num_1, num_2))
            case '*':
                print(multiply(num_1, num_2))
            case '/':
                print(multiply(num_1, num_2))
            
calculator()    


    
   
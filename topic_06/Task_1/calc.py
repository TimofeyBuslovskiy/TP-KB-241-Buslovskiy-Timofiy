from operation import get_num_for_user, get_operator, execute_number
from log import makeLog

def calculator () :
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
            result = execute_number(num_1, num_2, operator)
            makeLog(num_1, num_2, operator, result)
            print(f"Result is: {result}")

calculator()
        

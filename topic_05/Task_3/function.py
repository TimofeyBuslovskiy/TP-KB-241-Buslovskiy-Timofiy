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
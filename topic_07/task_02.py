class Calculator :
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
           return a / b


def main () :
    calc = Calculator()
    while True :
        num_1_inp = float(input("Ведіть перше число: "))        
        num_2_inp = float(input("Ведіть друге число: "))
        operator = input('Виберіть оператор: ')

        match operator :
            case "+" :
                result = calc.add(num_1_inp, num_2_inp)
            case "-" :
                result = calc.subtract(num_1_inp, num_2_inp)
            case "*" : 
                result = calc.multiply(num_1_inp, num_2_inp)
            case "/" :
                result = calc.divide(num_1_inp, num_2_inp)
            
        print(result)

main()
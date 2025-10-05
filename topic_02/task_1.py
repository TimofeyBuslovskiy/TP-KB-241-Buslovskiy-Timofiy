import math

def find_discriminant (a, b, c) :
    discriminant = b**2 - 4*a*c
    return discriminant

def find_quadratic_roots (a, b, c) :
    D = find_discriminant(a, b, c)
    if D > 0 :
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*b)
        return x1, x2
    elif D == 0 :
        x = -b / (2*a)
        return x
    else :
        ans = 'Не має коренів'
        return ans
    
a = float(input('Введіть перше число: '))
b = float(input('Введіть друге число: '))
c = float(input('Введіть третє число: '))

print(find_quadratic_roots(a, b, c))
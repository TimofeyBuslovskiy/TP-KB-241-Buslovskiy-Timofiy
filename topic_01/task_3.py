def find_discriminant (a, b, c) :
    discriminant = b**2 - 4*a*c
    return discriminant

a = float(input('Input a: '))
b = float(input('Input b: '))
c = float(input('Input c: '))

disc = find_discriminant(a, b, c)

print( disc )
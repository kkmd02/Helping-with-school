import math

def quadratic_formula(a, b, c):
    disc = b**2 - 4*a*c
    if disc > 0:
        r1 = (-b + math.sqrt(disc)) / (2 * a)
        r2 = (-b - math.sqrt(disc)) / (2 * a)
        print ('the roots are', str(r1), 'and', str(r2))
    elif disc == 0:
        print ('the root is 0')
    else:
        print ('There are no rational roots')








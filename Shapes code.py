import math

#only works for isoselese trapazoid
def trap_measure_perimeter(side1, side2, hieght):
    base_triangle = abs(side1-side2)
    theta = math.atan(2*hieght/base_triangle)
    side3 = hieght/ math.sin(theta)
    perimeter = side1 + side2 + 2*side3
    print ("Perimiter is: " + str(perimeter))

def trap_measure_area(side1, side2, hieght):
    area = hieght*(side1 + side2)/2
    print("Area is: " + str(area))

def evaluate_trapazoid(side1, side2, hieght):
    trap_measure_area(side1, side2, hieght)
    trap_measure_perimeter (side1, side2, hieght)

#square
def square_measure_perimeter(side):
    perimeter = 4*side
    print ("Perimiter is: " + str(perimeter))

def square_measure_area(side):
    area = side**2
    print ("Area is: " + str(area))

def evaluate_square(side):
    square_measure_area(side)
    square_measure_perimeter(side)

#decagon
def decagon_measure_perimeter(side):
    perimeter = 10*side
    print ("Perimiter is: " + str(perimeter))

def decagon_measure_area(side):
    area = 5/2*side**2*(5+2*(5**(1/2)))**(1/2)
    print ("Area is: " + str(area))

def evaluate_decagon(side):
    decagon_measure_area(side)
    decagon_measure_perimeter(side)

#triangle
def eq_riangle_measure_perimeter(side):
    perimeter = side*3
    print('perimeter is: ' + str(perimeter))

#why is sin60 -ve
#cuz it's in rad
def eq_triangle_measure_area(side):
    height = math.sin(math.pi/3) * side
    area= side*height/2
    print('area is:', area)

def evaluate_eq_triangle (side):
    triangle_measure_area(side)
    triangle_measure_perimeter(side)

#isoceles triangle
def iso_triangle_measure_area(base, sides):
    height = math.sin(math.pi/4) * sides
    area = base*height / 2
    print ("Area is:", area)

def iso_triangle_measure_perimeter(base, sides):
    perimeter = base+ 2* sides
    print ('Perimeter is:', perimeter)

def evaluate_iso_triangle(base, sides):
    iso_triangle_measure_area(base, sides)
    iso_triangle_measure_perimeter (base, sides)

if __name__ == "__main__":
    evaluate_iso_triangle(2, 22)






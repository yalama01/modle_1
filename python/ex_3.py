#Take in an integer greater than 1. Print out the cubes of each integer from 0 to the inputted integer\

integer = int(input("Enter an integer greater than 1: "))
for i in range(0, integer + 1):
    print("the cube of: ",i,i ** 3)

row = int(input("Enter a row number from 1 to 5: "))
column = int(input("Enter a column number from 1 to 5: "))
for i in range(1, row+1):
    for j in range(1, column+1):
        if i == row and j == column:
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()

    
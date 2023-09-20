n = int(input("Enter a number: "))
list = []
for i in range(0, n):
    list.append(float(input("Enter a float: ")))
print(list)
print(sum(list)/len(list))
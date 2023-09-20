
list1 = []
list2 = []
while True:
    string = input("Enter an integer or QUIT: ")
    if string == "QUIT":
        break
    else:
        list1.append(int(string))
for i in range(0, len(list1)):
    if list1[i] % 2 == 0:
        list2.append(list1[i])

print("list1",list1)
print("even list",list2)



#Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store them in a separate list. Create a third array containing the common values from both arrays without duplicates. Print out all three lists.

list1 = []
list2 = []
list3 = []
print("list1:")
for i in range(0, 5):
    list1.append(int(input("Enter an integer: ")))
print("list1",list1)
print("list2:")
    
for i in range(0, 5):
    list2.append(int(input("Enter an integer: ")))
    
for i in range(0, 5):
    if list1[i] in list2:
        list3.append(list1[i])
print("list1",list1)
print("list2",list2)
print("list3",list3)
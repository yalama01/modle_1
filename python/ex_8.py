
list1 = []
for i in range(0, 10):
    list1.append(int(input("Enter an integer: ")))


num_count = {}
for num in list1:
    if num in num_count:
        num_count[num] += 1
    else:
        num_count[num] = 1

unique_elements = [num for num, count in num_count.items() if count == 1]

print("Original list:", list1)
print("New list with elements that appear once:", unique_elements)
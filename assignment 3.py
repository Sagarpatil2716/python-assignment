# Taking series of numbers
list1 = [10,21,4,45,66,93,11]

even_count = 0
odd_count = 0
num = 0

# Using while loop
while(num < len(list1)):
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num += 1    
print("Count of Even numbers in the list : ", even_count)
print("Count of Odd numbers in the list : ", odd_count)
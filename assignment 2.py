# Doing a string reverse using for loop and range as explained in class 
str = input("Enter the String : ")
s = len(str) + 1
print("Original String is : ", end="")
print(str)
print("The Reversed String is : ", end="")
for i in range(-1, -s , -1):
    print(str[i], end="") 
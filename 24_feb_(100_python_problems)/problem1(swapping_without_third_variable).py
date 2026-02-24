#swapping of two number without third variable
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))

# Swap using arithmetic operations
a = a + b
b = a - b
a = a - b
print("after swapping")
print("first number is ",a)
print("second number is ",b)

'''output 
Enter first number :34
Enter second number :36
after swapping
first number is  36
second number is  34
'''

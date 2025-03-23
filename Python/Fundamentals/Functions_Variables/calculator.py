
#this file will take two numbers and divide them, then print the result with two decimal places

x = float(input("Give me the first number: "))
y = float(input("Give me the second number: "))


z = x / y


#I can use f strings to round the result of a math operation
print(f"{z:.2f}")
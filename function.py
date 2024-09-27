# Function to calculate sum of two numbers
def calculate_sum(num1, num2):
    s=num1 + num2
    return s

# Function to calculate difference of two numbers
def calculate_difference(num1, num2):
    d=num1 - num2
    return d


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))


sum_result = calculate_sum(number1, number2)
difference_result = calculate_difference(number1, number2)

# Printing the results
print("The sum of ",number1, "and" ,number2,"is:", sum_result )
print("The difference of ",number1, "and" ,number2,"is:",difference_result )

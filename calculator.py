#Calculator
#Calculator logo
from art import logo

print(logo)

"""
Add is the function for sum
"""
def add(n1, n2):
    return n1 + n2

"""
Subtract is the function for subtraction
"""
def subtract(n1, n2):
    return n1 - n2

"""
Multiply is the function for multiplication
"""
def multiply(n1, n2):
    return n1 * n2

"""
Divide is the function for division
"""
def divide(n1, n2):
    return n1 / n2

#in the following code I'm asking the user which function would he like to use
operations = {
'+': add,
'-': subtract,
'*': multiply,
'/': divide
}

def calculator():
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    game = False

    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    #asking the user if he wants to continue making any calculations
    #I'm creating a while loop to let the user do as many operations as he wants.
    while game is not True:
        iteration = input(f"Type 'y' to continue calculating {first_answer}, or type 'n' to start a new calculation: ")
        if iteration == 'y':
            operation_symbol = input("Pick another operation: ")
            num3 = int(input("What's the next number?: "))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(first_answer, num3)
            print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
            first_answer = second_answer
        elif iteration == 'n':
            game = True
            calculator()
        else:
            print("You didn't type 'n' or 'y'")

calculator()

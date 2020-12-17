"""
Implement a safe number checker

Implement is_number(str) to return the numeric value of the string str if possible, otherwise return None
The checker works for strings representing non-negative integers.
The checker works for strings representing any integers.
The checker works for strings representing any numbers.
The checker returns either a number or None, and never raises an exception
"""

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

"""
Implement an operator checker

Implement is_valid_operator(operator) to return with True if the operator input parameter represents a valid operator, otherwise return with False.
Valid operators are the following: +, -, *, /.
"""

def is_valid_operator(operator):
    if operator in "+-*/":
        return True
    else:
        return False

"""
Implement an input number requester

Implement ask_for_a_number(force_valid_input) to return the numeric value of the user input. The function continuously ask an input from the user while
 it is not numeric when force_valid_input is True. When the force_valid_input is False and the user input is not numeric, the function returns with None.
The function asks an input from the user, e.g.: 'Please provide a number! '.
The function returns with the numeric value of the input string if it represents a valid number.
The function returns with None when the user input not represents any number and force_valid_input is False.
In case of force_valid_input is True, the function continuously ask for a number, while the provided input string not represents a valid number. After an
unsuccessful input, the program inform the user about the wrong input, e.g.: 'This didn't look like a number, try again.'.
 """
def ask_for_a_number(*force_valid_input):
    if not force_valid_input:
        force_valid_input=input("Please provide a number! ")
        while is_number(force_valid_input)!=True:
            print("This didn't look like a number, try again.")
            force_valid_input = input("Please provide a number! ")
        return force_valid_input

"""
Implement an operator requester

Implement ask_for_an_operator(force_valid_input) to return with a valid operator. The function continuously ask an operator from the user while it
is not valid operator when force_valid_input is True. When the force_valid_input is False and the user input is not a valid operator, the function
returns with None.
The function asks an input from the user, e.g.: 'Please provide an operator (one of +, -, *, /)! '.
The function returns with an operator if the input string represents a valid operator.
The function returns with None when the user input not represents valid operator and force_valid_input is False.
In case of force_valid_input is True, the function continuously ask for an operator, while the provided input string not represents a valid operator.
After an unsuccessful input, the program inform the user about the wrong input, e.g.: 'Unknown operator.'.
"""

def ask_for_an_operator(*force_valid_input):
    if not force_valid_input:
        force_valid_input=input("Please provide an operator! ")
        while is_valid_operator(force_valid_input)!=True:
            print("This didn't look like an operator, try again.")
            force_valid_input = input("Please provide an operator! ")
    return force_valid_input

"""
Implement the calculator core

Implement calc(operator, a, b) to calculate the result of the 'a' 'operator' 'b' operator. The function returns with None if any operand or the operator 
is not valid. The function handles division by zero, in this case the return value is None
The function checks the validity of the operands and the operator. Returns with None in case of any invalid input.
The function returns with the result of 'a' + 'b' if the operator is '+'.
The function returns with the result of 'a' - 'b' if the operator is '-'.
The function returns with the result of 'a' * 'b' if the operator is '*'.
The function returns with the result of 'a' / 'b' if the operator is '/' and b is not equal to 0. If the 'b' is equal to 0, the function prints an error 
message, e.g.: 'Error: Division by zero' and returns with None.
"""

def calc(operator, a, b):
    try:
        if operator == "+":
            return "The result is "+ str(int(a)+int(b))
        if operator == "-":
            return "The result is "+ str(int(a)-int(b))
        if operator == "*":
            return "The result is "+ str(int(a)*int(b))
        if operator == "/":
            return "The result is "+ str(int(a)/int(b))
    except ZeroDivisionError as err:
        print(err)

"""
Implement the main calculator logic

Implement simple_calculator() to create the calculator. The function continuously asks for number 'a' and 'b' and an operator and calculates the result of 
'a' 'operator' 'b'.
The function checks the validity of the operands and the operator. Exit from the program if the 'a' operand is not valid. In case of valid 'a' operand, the
 function ensures the operand 'b' and the operator is valid.
The function prints the calculation results, e.g.: 'The result is 10'.
"""
def simple_calculator():
    a=ask_for_a_number()
    operator=ask_for_an_operator()
    b=ask_for_a_number()
    return calc(operator,a,b)

print(simple_calculator())



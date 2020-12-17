"""
4.Create and call two functions in helloinput.py - one should ask for the name of the user and an another which prints the custom greeting message to the console
Running helloinput.py prints What's your name?, asks for user input, and using the input prints Hello, <name>! to the console
Running helloinput.py asks What's your name?, and if the user does not enter anything, it prints Hello, World! to the console
The source code of helloinput.py defines a get_hello_message() function which prints What's your name?, and returns Hello, <name>! using the user
input (or Hello, World! for an empty input)
The source code of helloinput.py defines and calls a say_hello() function which is responsible for printing the message returned by get_hello_message()
Hello, Argument!
"""


def get_hello_message():
    name=input("What's your name? ")
    if not name:
        name="World!"
    return f"Hello, " + name + " !"

def say_hello():
    message=get_hello_message()
    print(message)
say_hello()

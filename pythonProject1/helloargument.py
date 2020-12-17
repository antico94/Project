"""
5.Capitalize the user's diplayed name in a reorganized helloargument.py that separates the input collection and the message assembly parts
Running helloargument.py prints What's your name?, asks for user input, and using the input prints Hello, <Name>! to the console (<Name> is capitalized)
Running helloargument.py asks What's your name?, and if the user does not enter anything, it prints Hello, World! to the console
The source code of helloinput.py defines a get_user_name() function which prints What's your name?, and returns the capitalized version of the user's input string
The source code of helloinput.py defines a get_hello_message(name) function which returns Hello, <name>! using the incoming argument (or Hello, World! for an empty argument)
The source code of helloinput.py defines and calls a say_hello() function which is responsible for printing the message after collecting the returned values from the other
 two functions
General requirements
None
"""

def get_user_name():
    name=input("What's your name? ")
    name=name.capitalize()
    return name

def get_hello_message(name):
    if not name:
        name="World"
    return f"Hello, "+ name + "!"

def say_hello():
    username = get_user_name()
    message= get_hello_message(username)
    print(message)
say_hello()
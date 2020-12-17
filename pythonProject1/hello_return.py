"""

3.Create and call two functions in helloreturn.py - one should return the Hello, World! string to the another which prints this message to the console
Running helloreturn.py prints out Hello, World! to the console
The source code of helloreturn.py defines a get_hello_message() function which does not print anything but returns the Hello, World! message
The source code of helloreturn.py defines and calls a say_hello() function which is responsible for printing the message returned by get_hello_message()
Hello, Input!
"""
def get_hello_message():
    return f"Hello, World!"

def say_hello():
    message = get_hello_message()
    print(message)
say_hello()


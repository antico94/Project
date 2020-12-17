"""








"""

"""
min()

Implement the min(x, y) function for two real numbers as inputs!
For any two real numbers the less is returned
No built-in functions are used
max()
"""


def min(x,y):
    x=float(x)
    y=float(y)
    if x>=y:
        y=str(y)
        print("The smaller number is: " + y)
    else:
        x=str(x)
        print("The smaller number is: " + x)
min(.2,2.3)

"""
Implement the max(values_list) function for a list of numbers!
For any list of real numbers the greatest is returned
No built-in functions are used
len()
"""

def max(values_list):
    list=[]
    big=0
    for number in values_list:
        list.append(number)
        number=int(number)
        if big>number:
            big=big
        else:
            big=number
    print("The max is :"+ str(big))
max([1,2,3,4,5,6])


"""
Implement the len(values_list) function for a list of numbers or strings which returns the length of the list!
For any list the count of the elements is returned
No built-in functions are used
multiply()
"""

def len(values_list):
    i=0
    for char in values_list:
        i+=1
    print("The lenght of the list is " +str(i))
len("Hello worl")

"""
Implement the multiply(x, y) function for integer numbers as inputs! Do not use the *, /, and // operators and any built-in functions, but you may (and should)
use +.
For any two integer inputs the returned value equals the result of x * y
Neither *, /, // nor any built-in functions are used
pow()
"""

def multiply(x,y):
    int(x)
    int(y)
    list=[]
    sum=0

    for number in range(y):
                list.append(x)
    for number in list:
                sum=sum+number
    print("The result of the multiply: " + str(sum))
multiply(6,0)



"""
Implement the pow(x, y) function for real base numbers and positive integer exponents! Do not use the ** operator and any built-in functions! Here you can use *.
For inputs from the specified domain the returned value equals the result of x**y
Neither ** nor any built-in functions are used
divmod()
"""

def pow(x,y):
    float(x)
    float(y)
    list=[]
    mul=1
    if x==0:
        print("Pow of x at y is: 1")
    else:
         for number in range(y):
            list.append(x)
         for number in list:
            mul=mul*number
         print("Pow of x at y is: "+ str(mul))
pow(7,8)

"""
OPTIONAL Implement the divmod(x,y) function for for two integer numbers as inputs! Do not use the // and the % operators and any built-in functions!
It should return a tuple: the first value should be equal to the value of x // y and the second equal to the value of x % y! Do not use the // operator
and any built-in functions!
For any two positive integer inputs the returned value equals (x // y, x % y)
For any two +/- integer inputs the returned value equals (x // y, x % y)
Neither // nor any built-in functions are used
"""

def divmod(x,y):
    int(x)
    int(y)
    div=int(x/y)
    int(div)
    rest=x-(y*div)
    print("The result is: (" + str(int(div)) + "," + str(int(rest))+ ").")
divmod(-18,7)








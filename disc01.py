# Q1.1
# Alfonso will only wear a jacket outside if it is below 60 degrees or it is
# raining. Write a function that takes in the current temperature and a
# boolean value telling if it is raining and returns True if Alfonso will wear
# a jacket and False otherwise.
# First, try solving this problem using an if statement.
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    if temp < 60 or raining:
        return True
    else:
        return False

# Note that we’ll either return True or False based on a single condition,
# whose truthiness value will also be either True or False. Knowing this, try
# to write this function using a single line.
def wears_jacket(temp, raining):
    return temp < 60 or raining

# Q1.2
# What is the result of evaluating the following code?
def square(x):
    print("here!")
    return x * x

def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0
    """
    >>> square(so_slow(5))
    Nothing (infinite loop)
    """

# Q1.3
# Tutorial: Write a function that returns True if a positive integer n is a
# prime number and False otherwise.

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = n - 1
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

# Q2.1
# Use these rules to draw a simple diagram for the assignment statements below.
x = 10 % 4
y = x
x **= 2

# Global frame
#         x: 4
#         y: 2

# Q2.2
# Use these rules and the rules for assignment statements to draw a diagram
# for the code below.
def double(x):
    return x * 2

def triple(x):
    return x * 3

hat = double
double = triple

# Global frame
#     double -> func triple(x) [parent = Global]
#     triple -> func triple(x) [parent = Global]
#     hat    -> func double(x) [parent = Global]

# Q2.3
# Let’s put it all together! Draw an environment diagram for the following code.
def double(x):
    return x * 2

hmmm = double
wow = double(3)
hmmm(wow)

# Global frame
#     double -> func double(x) [parent = Global]
#     hmmm   -> func double(x) [parent = Global]
#     wow: 6

# f1 double [parent = Global]
#     x: 3
#     return value: 6

# f2 double [parent = Global]
#     x: 6
#     return value: 12

# Q2.4
# Tutorial: Draw the environment diagram that results from executing the code
# below.
def f(x):
    return x

def g(x, y):
    if x(y):
        return not y
    return y
    
x = 3
x = g(f, x)
f = g(f, 0)

# Global frame
#     f: 0
#     g -> func g(x) [parent = Global]
#     x: False

# f1 g [parent = Global]
#     x -> func f(x) [parent = Global]
#     y: 3
#     return value: False

# f2 f [parent = Global]
#     x: 3
#     return value: 3

# f3 g [parent = Global]
#     x -> func f(x) [parent = Global]
#     y: 0
#     return value: 0

# f4 f [parent = Global]
#     x: 0
#     return value: 0

# Q1.1
# Write a function that takes in a function cond and a number n and prints
# numbers from 1 to n where calling cond on that number returns True.
def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1

# Q1.2
# Tutorial: Write a function similar to keep_ints like before, but now it
# takes in a number n and returns a function that has one parameter cond.
# The returned function prints out numbers from 1 to n where calling cond on
# that number returns True.
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def keeper(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return keeper

# Q1.3
# Draw the environment diagram that results from executing the code below.
def curry2(h):
    def f(x):
        def g(y):
            return h(x, y)
        return g
    return f
make_adder = curry2(lambda x, y: x + y)
add_three = make_adder(3)
add_four = make_adder(4)
five = add_three(2)

# Global frame
#     curry2     -> func curry2(h) [parent = Global]
#     make_adder -> func f(x) [parent = f1]
#     add_three  -> func g(y) [parent = f2]
#     add_four   -> func g(y) [parent = f3]
#     five: 5

# f1 curry2 [parent = Global]
#     h -> func lambda(x, y) [parent = Global]
#     f -> func f(x) [parent = f1]
#     return value -> func f(x) [parent = f1]

# f2 f [parent = f1]
#     x: 3
#     g -> func g(y) [parent = f2]
#     return value -> func g(y) [parent = f2]

# f3 f [parent = f1]
#     x: 4
#     g -> func g(y) [parent = f3]
#     return value -> func g(y) [parent = f3]

# f4 g [parent = f2]
#     y: 2
#     return value: 5

# f5 lambda [parent = Global]
#     x: 3
#     y: 2
#     return value: 5

# Q1.4 Write curry2 as a lambda function
lambda_curry2 = lambda h: lambda x: lambda y: h(x, y)

# Q1.5 Tutorial: Draw the environment diagram that results from executing the 
# code below.

n = 7

def f(x):
    n = 8
    return x + 1

def g(x):
    n = 9
    def h():
        return x + 1
    return h

def f(f, x):
    return f(x + n)

f = f(g, n)
g = (lambda y: y())(f)

# Global frame
#     n: 7
#     g: 15
#     f -> func h() [parent = f2]

# f1 f [parent = Global]
#     f -> func g(x) [parent = Global]
#     x: 7
#     return value -> func h() [parent = f2]

# f2 g [parent = Global]
#     x: 14
#     n: 9
#     h -> func h() [parent = f2]
#     return value -> func h() [parent = f2]

# f3 lambda [parent = Global]
#     y -> func h() [parent = f2]
#     return value: 15

# f4 h [parent = f2]
#     return value: 15

# Q1.6
# The following question is more challenging than the previous ones. 
# Nonetheless, it’s a fun problem to try.
# Draw the environment diagram that results from executing the code below.
# Note that using the + operator with two strings results in the second string
# being appended to the first. For example "C" + "S" concatenates the two
# strings into one string "CS"
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
y = y(y)(y)

# Global frame
#     h: "y"
#     y: "hi"

# f1 y [parent = Global]
#     y -> func lambda(y) <line 7> [parent = f1]
#     h: "h"
#     return value -> func lambda(h) <line 8> [parent = f1]

# f2 lambda <line 8> [parent = f1]
#     h -> func y(y) [parent = Global]
#     return value: "hi"

# f3 lambda <line 7> [parent = f1]
#     y -> func y(y) [parent = Global]
#     h: "h"
#     return value: "hi"

# f4 y [parent = Global]
#     y: "h"
#     h: "h"
#     return value: "hi"

# Write a function print delayed that delays printing its argument until the
# next function call. print delayed takes in an argument x and returns a
# new function delay print. When delay print is called, it prints out x and
# returns another delay print.
def print_delayed(x):
    """Return a new function. This new function, when called,
    will print out x and return another function with the same
    behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi")
    5
    <function print_delayed> # a function is returned
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# Q1.8
# Tutorial: Write a function print n that can take in an integer n and returns
# a repeatable print function that can print the next n parameters. After the
# nth parameter, it just prints ”done”.
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n < 1:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

# What Would Python Display?
# Q1: WWPD: Lambda the Free
# For all WWPD questions, type Function if you believe the answer is
# <function...>, Error if it errors, and Nothing if nothing is displayed. As a
# reminder, the following two lines of code will not display anything in the
# Python interpreter when executed:
# >>> x = None
# >>> x

# >>> lambda x: x  # A lambda expression with one parameter x
# Function
# >>> a = lambda x: x  # Assigning the lambda function to the name a
# >>> a(5)
# 5
# >>> (lambda: 3)()  # Using a lambda expression as an operator in a call exp.
# 3
# >>> b = lambda x: lambda: x  # Lambdas can return other lambdas!
# >>> c = b(88)
# >>> c
# Function
# >>> c()
# 88
# >>> d = lambda f: f(4)  # They can have functions as arguments as well.
# >>> def square(x):
# ...     return x * x
# >>> d(square)
# 16
 
# >>> x = None # remember to review the rules of WWPD given above!
# >>> x
# >>> lambda x: x
# Function
 
# >>> z = 3
# >>> e = lambda x: lambda y: lambda: x + y + z
# >>> e(0)(1)()
# 4
# >>> f = lambda z: x + z
# >>> f(3)
# Error
 
# >>> higher_order_lambda = lambda f: lambda x: f(x)
# >>> g = lambda x: x * x
# >>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?
# Error
# >>> higher_order_lambda(g)(2)
# 4
# >>> call_thrice = lambda f: lambda x: f(f(f(x)))
# >>> call_thrice(lambda y: y + 1)(0)
# 3
# >>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
# >>> print_lambda
# Function
# >>> one_thousand = print_lambda(1000)
# 1000
# >>> one_thousand
# Nothing

# Q2: WWPD: Higher Order Functions
def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd
    """
    >>> steven = lambda x: x
    >>> stewart = even(steven)
    >>> stewart
    Function
    >>> stewart(61)
    61
    >>> stewart(-4)
    4
    """

def cake():
    print('beets')
    def pie():
        print('sweets')
        return 'cake'
    return pie
    """
    >>> chocolate = cake()
    beets
    >>> chocolate
    Function
    >>> chocolate()
    sweets
    'cake'
    >>> more_chocolate, more_cake = chocolate(), cake
    sweets
    >>> more_chocolate
    'cake'
    """

def snake(x, y):
    if cake == more_cake:
        return chocolate
    else:
        return x + y
    """
    >>> snake(10, 20)
    Function
    >>> snake(10, 20)()
    sweets
    'cake'
    >>> cake = 'cake'
    >>> snake(10, 20)
    30
    """

# Coding Practice
# Q3: Lambdas and Currying
 
# Write a function lambda_curry2 that will curry any two argument function using
# lambdas. Refer to the textbook for more details about currying.
 
# Your solution to this problem should fit entirely on the return line. You can
# try writing it first without this restriction, but rewrite it after in one
# line.

from operator import add, mul, mod
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    return lambda x: lambda y: func(x, y)

# Q4: Count van Count
# Consider the following implementations of count_factors and count_primes:

def count_factors(n):
    """Return the number of positive factors that n has.
    >>> count_factors(6)
    4   # 1, 2, 3, 6
    >>> count_factors(4)
    3   # 1, 2, 4
    """
    i, total= 1, 0
    while i <= n:
        if n % i == 0:
            total += 1
        i += 1
    return total

def count_primes(n):
    """Return the number of prime numbers up to and including n.
    >>> count_primes(6)
    3   # 2, 3, 5
    >>> count_primes(13)
    6   # 2, 3, 5, 7, 11, 13
    """
    i, total = 1, 0
    while i <= n:
        if is_prime(i):
            total += 1
        i += 1
    return total

def is_prime(n):
    return count_factors(n) == 2 # only factors are 1 and n

# The implementations look quite similar! Generalize this logic by writing a
# function count_cond, which takes in a two-argument predicate function
# condition(n, i). count_cond returns a one-argument function that takes in N,
# which counts all the numbers from 1 to N that satisfy condition when called.

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N.

    >>> count_factors = count_cond(lambda n, i: n % i == 0)
    >>> count_factors(2)   # 1, 2
    2
    >>> count_factors(4)   # 1, 2, 4
    3
    >>> count_factors(12)  # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_factors(i) == 2
    >>> count_primes = count_cond(is_prime)
    >>> count_primes(2)    # 2
    1
    >>> count_primes(3)    # 2, 3
    2
    >>> count_primes(4)    # 2, 3
    2
    >>> count_primes(5)    # 2, 3, 5
    3
    >>> count_primes(20)   # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"
    def f(n):
        i, total = 1, 0
        while i <= n:
            if condition(n, i):
                total += 1
            i += 1
        return total
    return f

# Q5: Make Adder
# Draw the environment diagram for the following code:
n = 9
def make_adder(n):
    return lambda k: k + n
add_ten = make_adder(n+1)
result = add_ten(n)

# Global
# n: 9
# make_adder -> make_adder(n) [parent = Global] 
# add_ten -> lambda(k) <line 3> [parent = f1]
# result: 19

# f1 make_adder [parent = Global]
# n: 10
# return value -> lambda(k) <line 3> [parent = f1]

# f2 lambda <line 3> [parent = f1]
# k: 9
# return value: 19

# Q6: Lambda the Environment Diagram
# Try drawing an environment diagram for the following code and predict what
# Python will output.

# >>> a = lambda x: x * 2 + 1
# >>> def b(b, x):
# ...     return b(x + a(x))
# >>> x = 3
# >>> b(a, x)
# 21

# Global
# a -> lambda(x) <line 1> [parent = Global]
# b -> b(b, x) [parent = Global]
# x: 3


# f1 b [parent = Global]
# b -> lambda(x) <line 1> [parent = Global]
# x: 3
# return value: 21

# f2 lambda <line 1> [parent = Global]
# x: 3
# return value: 7

# f3 lambda <line 1> [parent = Global]
# x: 10
# return value: 21

# Q7: Composite Identity Function
# Write a function that takes in two single-argument functions, f and g, and
# returns another function that has a single parameter x. The returned function
# should return True if f(g(x)) is equal to g(f(x)). You can assume the output
# of g(x) is a valid input for f and vice versa. Try to use the compose1
# function defined below for more HOF practice.
def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    "*** YOUR CODE HERE ***"
    def id_check(x):
        return f(g(x)) == g(f(x))
    return id_check

# Q8: I Heard You Liked Functions...
# Define a function cycle that takes in three functions f1, f2, f3, as
# arguments. cycle will return another function that should take in an integer
# argument n and return another function. That final function should take in an
# argument x and cycle through applying f1, f2, and f3 to x, depending on what n
# was. Here's what the final function should do to x for a few values of n:
# 
# n = 0, return x
# n = 1, apply f1 to x, or return f1(x)
# n = 2, apply f1 to x and then f2 to the result of that, or return f2(f1(x))
# n = 3, apply f1 to x, f2 to the result of applying f1, and then f3 to the result of applying f2, or f3(f2(f1(x)))
# n = 4, start the cycle again applying f1, then f2, then f3, then f1 again, or f1(f3(f2(f1(x))))
# And so forth.
# Hint: most of the work goes inside the most nested function.

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
    def f_n(n):
        def f_x(x):
            i = 0
            while i < n:
                if i%3 == 0:
                    x = f1(x)
                elif i%3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return f_x
    return f_n

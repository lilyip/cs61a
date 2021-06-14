# What Would Python Display? (Part 1)
# Q1: WWPD: Control
def xk(c, d):
    if c == 4:
        return 6
    elif d >= 4:
        return 6 + 7 + c
    else:
        return 25
    
    """
    >>> xk(10, 10)
    23
    >>> xk(10, 6) 
    23
    >>> xk(4, 6)
    6
    >>> xk(0, 0)
    25
    """

def how_big(x):
    if x > 10:
        print('huge')
    elif x > 5:
        return 'big'
    elif x > 0:
        print('small')
    else:
        print("nothin")

    """
    >>> how_big(7)
    'big'
    >>> how_big(12)
    huge
    >>> how_big(1)
    small
    >>> how_big(-1)
    nothin
    """

# positive = 28
# while positive:
#     print("positive?")
#     positive -= 3
# <infinite loop> positive is never 0

# positive = -9
# negative = -12
# while negative:
#     if positive:
#         print(negative)
#     positive += 3
#     negative += 3
# -12
# -9
# -6

# Q2: WWPD: Veritasiness
# >>> True and 13
# True
# >>> False or 0
# False
# >>> not 10
# False
# >>> not None
# True

# >>> True and 1 / 0 and False
# <error>
# >>> True or 1 / 0 or False
# True
# >>> True and 0
# 0
# >>> False or 1
# 1
# >>> 1 and 3 and 6 and 10 and 15
# 15
# >>> -1 and 1 > 0
# True
# >>> 0 or False or 2 or 1 / 0
# 2

# >>> not 0
# True
# >>> (1 + 1) and 1
# 1
# >>> 1/0 or True
# <error>
# >>> (True or False) and False
# False

# Q3: Debugging Quiz!
# (Must use courseware. Registered students only)

# Q4: Falling Factorial
# Let's write a function falling, which is a "falling" factorial that takes
# two arguments, N and K, and returns the product of K consecutive numbers,
# starting from N and working downwards.
def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    stop, total = n - k, 1
    if k == 0:
        return total
    else:
        while n > stop:
            total *= n
            n -= 1
        return total

# Q5: Sum Digits
# Write a function that takes in a nonnegative integer and sums its digits.
# (Using floor division and modulo might be helpful here!)
def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    i, j, total = 1, 1, y % 10
    while j > 0:
        j = (y // pow(10, i)) % 10
        total += j
        i += 1
    return total

# Q6: WWPD: What If?
def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')
    """
    >>> ab(10, 20)
    10
    foo
    """

def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make
    """
    >>> bake(0, 29)
    1
    29
    29
    """

# Q7: Double Eights
# Write a function that takes in a number and determines if 
# the digits contain two adjacent 8s.
def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    i, j, prevj, dubs = 1, 1, n % 10, False
    while j > 0:
        j = (n // pow(10, i)) % 10
        if j == prevj == 8:
            dubs = True
        prevj = j
        i += 1
    return dubs

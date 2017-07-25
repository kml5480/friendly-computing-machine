"""
A small set of functions for doing math operations.

"""


# Write a function named add that adds two values.
def add(A, B):
    """
    Function for adding two values.
    """
    return A + B

# Write a function that multiplies two values.
def multiply(A, B):
    """
    Function for multiplying two values.
    """
    return A * B

def subtract(A, B):
    """
    Function for subtracting a value B from a value A.
    """
    return A - B

def divide(A, B):
    """
    Function for dividing a value A by a value B.
    Always uses foating point division!
    """
    return float(A) / float(B)

def int_division(A, B):
    """
    Function for dividing integers (achieves truncation).
    """
    return A//B

def power(A, B):
    """
    Function for raising A to a power B.
    """

    pow = 1
    for i in range(B):
        pow *= A

    return pow

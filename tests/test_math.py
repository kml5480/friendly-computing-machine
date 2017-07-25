""" 
File testing math.py performance.
"""

import friendly_computing_machine as fcm
import numpy as np
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert np.allclose(fcm.math.add(2.1, 3.6), 5.7)

def test_multiply():
    assert fcm.math.multiply(1, 2) == 2
    assert fcm.math.multiply(3, 2) == 6
    assert np.allclose(fcm.math.multiply(2.4, 6.9), 16.56)
    assert fcm.math.multiply(1, 0) == 0

def test_subtract():
    assert fcm.math.subtract(10, 8) == 2
    assert fcm.math.subtract(8, 10) == -2
    assert np.allclose(fcm.math.subtract(5.6, 3.1), 2.5) 

def test_divide():
    assert fcm.math.divide(10, 2) == 5.0
    assert fcm.math.divide(10, 4) == 2.50
    assert np.allclose(fcm.math.divide(6.3, 2.4), 2.625)

def test_int_division():
    assert fcm.math.int_division(10, 2) == 5
    assert fcm.math.int_division(10, 3) == 3
    assert fcm.math.int_division(10, 4) == 2

def test_power():
    assert fcm.math.power(2, 0) == 1
    assert fcm.math.power(1, 5) == 1
    assert fcm.math.power(2, 4) == 16
    assert fcm.math.power(3, 3) == 27


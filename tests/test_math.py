""" 
File testing math.py performance.
"""

import friendly_computing_machine as fcm
import pytest

def test_add():
    assert fcm.math.add(5, 2) == 7
    assert fcm.math.add(2, 5) == 7


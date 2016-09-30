from pytest import raises
from binsearch import binary_search
import numpy as np

def test_normal():
    input_array = list(range(10))
    assert binary_search(input_array,5) == 5

def test_decimal():
    input_array = list(range(10))
    assert binary_search(input_array,4.5) == -1

def test_border():
    input_array = list(range(10))
    assert binary_search(input_array,10) == -1

def test_one_T():
    assert binary_search([5],5) == 0

def test_one_F():
    assert binary_search([5],4) == -1

def test_inf_1():
    assert binary_search([1,2,np.inf],2) == 1

def test_inf_2():
    assert binary_search([1,2,np.inf],np.inf) == 2

def test_bound_F():
    input_array = list(range(10))
    assert binary_search(input_array, 5, 1, 3) == -1

def test_bound_T():
    input_array = list(range(10))
    assert binary_search(input_array, 2, 1, 3) == 2

def test_bound_reverse():
    input_array = list(range(10))
    assert binary_search(input_array, 2, 3, 1) == -1

def test_bound_same():
    input_array = list(range(10))
    assert binary_search(input_array, 2, 2, 2) == 2

def test_bound_outflow():
    input_array = list(range(10))
    assert binary_search(input_array, 5, 2, 2) == -1

def test_char():
    with raises(TypeError):
        binary_search(‘a’, 2)

def test_zero():
    with raises(ValueError):
        mymedian([])

def test_nan_1():
    with raises(ValueError):
        mymedian([1, nan], 1)

def test_nan_2():
    with raises(ValueError):
        mymedian([1, nan], nan)

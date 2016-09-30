from pytest import raises
from binsearch import binary_search
import numpy as np

def test_normal():
	input_array = list(range(10))
	assert binary_search(input_array,5) == 5
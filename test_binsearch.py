from pytest import raises
from binsearch import binary_search

def test_one_element():
	assert binary_search([5],5) == 0
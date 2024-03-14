import sys
sys.path.append('../')
from CICD.main import calculate_area_square
import pytest

def test_clculate_area_square():
    assert calculate_area_square(2) == 4
    assert calculate_area_square(2.5) == 6.25

def test_clculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-1)

def test_clculate_area_square_string():
    with pytest.raises(TypeError):
        calculate_area_square('hello')

def test_clculate_area_square_list():
    with pytest.raises(TypeError):
        calculate_area_square([1,2])


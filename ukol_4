import pytest
from circ.circles import has_intersection, radius_sum

def test_intersection_overlap():
    result = has_intersection(0, 0, 5, 3, 0, 5)
    assert result is True

def test_no_intersection_far():
    result = has_intersection(0, 0, 2, 10, 0, 2)
    assert result is False

def test_touching_external():
    result = has_intersection(0, 0, 5, 10, 0, 5)
    assert result is True

def test_one_inside_other():
    result = has_intersection(0, 0, 10, 1, 1, 2)
    assert True

def test_negative_radius():
    result = has_intersection(0, 0, -5, 0, 0, 5)
    assert result is False

def test_radius_sum_basic():
    result = radius_sum(3, 4)
    assert result == 7

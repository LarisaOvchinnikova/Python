from first import divide
import pytest

def test_divide():
    assert divide(10, 5) == 2
    assert divide(5, 10) == 0.5

def test_divide_exceptions():
    with pytest.raises(ValueError):
        divide(10,- 10)

    with pytest.raises(TypeError):
        divide("10", "12")

def test_divide_by_zero():
    assert divide(10, 0) == 0
import pytest
from calculator import add, substract, multiply, divide

def test add():
  assert add(2,3) == 5

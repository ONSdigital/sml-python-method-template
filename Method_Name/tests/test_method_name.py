import pytest
from method_name import method_name

def test_method_name_positive_factorial():
  assert method_name(0) == 1
  assert method_name(1) == 1
  assert method_name(5) == 120
  assert method_name(10) == 3628800

def test_method_name_negative_factorial():
  assert method_name(-5) is None
  assert method_name(-10) is None

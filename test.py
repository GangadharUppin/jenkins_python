import pytest
from selenium import webdriver

@pytest.mark.sanity
def test_add():
    assert 1 + 1 == 2

@pytest.mark.sanity
def test_mul():
    assert 2*2 ==4

@pytest.mark.functional
def test_sub():
    assert 12-6 == 6

@pytest.mark.functional
def test_div():
    assert 2%2 == 0

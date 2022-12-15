#!/usr/bin/env python
# coding: utf-8
import pytest
import os

def compute_mean(data):
    """Compute the mean of a list of numbers
    Args:
        data (list): a list of numbers
    Returns:
        float: the mean value of the list
    """

    if len(data) == 0:
         return None
    else:
        mean = sum(data)/ len(data)
        return mean
    
@pytest.mark.skip(reason="test is bad")
def test_compute_mean():
    calc = compute_mean([0,10,20])
    assert calc == 10
    assert type(calc) == float
    calc = compute_mean([-10, 10])
    assert calc == 0    
    calc = compute_mean([0,10,0]) #define how many degits otherwise it will complain
    assert round(calc,4) == 3.3333 , "Check that average is correct"  
test_compute_mean()

@pytest.mark.skip(reason="test is bad")
def test_main():
    main()
    assert os.path.exists("plot_25.png")
test_main()


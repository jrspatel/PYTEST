from typing import List 

def sumi(lst : List[float]) -> float:
    """ takes i/p as list and outputs the float sum
    returns the sum of elements in the list """ 
    result = 0.0 
    for i in lst:
        result += i 
    return result 
"""" writing test cases and verifying them ..called unit testing """ 


from src.sum import sumi 

def test_sumi_mul():
    assert sumi([1,2,3]) == 6.0

def test_sumi_empty():
    assert sumi([]) == 0 

def test_sumi_single():
    assert sumi([5]) == 5.0
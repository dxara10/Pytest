def somar(a, b):
    return a + b
def subtrair(a, b):
    return a - b

def test_somar_subtrair():
    assert somar(2, 3) == 5
    assert subtrair(5, 3) == 2
    assert somar(-1, 1) == 0
    assert subtrair(-1, -1) == 0
    assert somar(0, 0) == 0
    assert subtrair(0, 0) == 0
    assert somar(1000000, 2000000) == 3000000
    assert subtrair(2000000, 1000000) == 1000000
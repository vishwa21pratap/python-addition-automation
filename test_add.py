from add import add

def test_add():
    assert add(1, 4) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

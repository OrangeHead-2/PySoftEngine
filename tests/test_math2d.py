from pysoftraster.core.math2d import Vec2

def test_add():
    a = Vec2(1, 2)
    b = Vec2(3, 4)
    result = a.add(b)
    assert result.x == 4 and result.y == 6, f"Expected (4,6), got ({result.x},{result.y})"

def test_subtract():
    a = Vec2(5, 7)
    b = Vec2(2, 3)
    result = a.subtract(b)
    assert result.x == 3 and result.y == 4, f"Expected (3,4), got ({result.x},{result.y})"

def test_dot():
    a = Vec2(1, 2)
    b = Vec2(3, 4)
    result = a.dot(b)
    assert result == 11, f"Expected dot product 11, got {result}"

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_dot()
    print("test_math2d passed.")
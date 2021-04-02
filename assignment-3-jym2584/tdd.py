import math

def test_triangle_height_invalid():
    result = triangle_height (-1)
    assert(result == None)
    print("Test Triangle Height Invalid passed")

def test_triangle_height_value():
    result = round(triangle_height (2), 5)
    assert(result == 1.73205)
    print("Test Triangle Height Value passed")

def triangle_height(base_length):
    if base_length < 0:
      return None
    return math.sqrt(base_length**2 - (base_length/2)**2)

def main():
    test_triangle_height_invalid()
    test_triangle_height_value()
main()
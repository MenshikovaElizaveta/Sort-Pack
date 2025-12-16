from sort_pack.bubble_sort import bubble_sort

# обычные unit-тесты

def test_first():
    first_arr = [0, 7, 3, 4]
    assert bubble_sort(first_arr) == [0, 3, 4, 7]

def test_second():
    second_arr = [766, 1, 9000, 23, 5248]
    assert bubble_sort(second_arr) == [1, 23, 766, 5248, 9000]
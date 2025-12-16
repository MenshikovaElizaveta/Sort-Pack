from sort_pack.quick_sort import quick_sort

# обычные unit-тесты

def test_first():
    first_arr = [0, 7, 3, 4]
    assert quick_sort(first_arr) == [0, 3, 4, 7]

def test_second():
    second_arr = [766, 1, 9000, 23, 5248]
    assert quick_sort(second_arr) == [1, 23, 766, 5248, 9000]
from sort_pack.heap_sort import heap_sort

# обычные unit-тесты

def test_first():
    first_arr = [0, 7, 3, 4]
    assert heap_sort(first_arr) == [0, 3, 4, 7]

def test_second():
    second_arr = [766, 1, 9000, 23, 5248]
    assert heap_sort(second_arr) == [1, 23, 766, 5248, 9000]
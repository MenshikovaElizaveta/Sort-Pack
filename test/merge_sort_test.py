from sort_pack.merge_sort import merge_sort

# обычные unit-тесты

def test_first():
    first_arr = [0, 7, 3, 4]
    assert merge_sort(first_arr) == [0, 3, 4, 7]

def test_second():
    second_arr = [766, 1, 9000, 23, 5248]
    assert merge_sort(second_arr) == [1, 23, 766, 5248, 9000]
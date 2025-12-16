def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    def separation(arr):
        runner = arr[-1]
        result = 0
        for i in range(len(arr) - 1):
            if arr[i] < runner:
                arr[i], arr[result] = arr[result], arr[i]
                result += 1
                
        arr[-1], arr[result] = arr[result], arr[-1]
        return arr, result

    arr, runner = separation(arr)
    arr[:runner] = quick_sort(arr[:runner])
    arr[runner + 1:] = quick_sort(arr[runner + 1:])
    
    return arr
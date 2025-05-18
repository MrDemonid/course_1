def qsort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]     # кладём в массив все эл. меньше pivot
    great = [i for i in array[1:] if i > pivot]     # кладём в массив все эл. больше pivot
    return qsort(less) + [pivot] + qsort(great)


def merge_sort(nums):
    if len(nums) <= 1:
        return
    # делим список надвое, пока в нем не осталось по одному элементу 
    mid = len(nums) // 2        # середина массива
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    # теперь сливаем два списка в один
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    # если остались какие-то значения, то добавляем их
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j  < len(right):
        nums[k] = right[j]
        j += 1
        k += 1



# python3

from random import randint


def partition3(array, left, right):
    x = array[left]
    lf = left
    ri = right
    i = left + 1
    while i <= ri:
        if array[i] < x:
            array[i], array[lf] = array[lf], array[i]
            lf += 1
            i += 1
        elif array[i] > x:
            array[i], array[ri] = array[ri], array[i]
            ri -= 1
        else:
            i += 1
    return lf, ri


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2+1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

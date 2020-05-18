# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    if len(a) < 2:
        return 0
    a_copy = a[:]
    new_list = [0] * len(a)
    return merge_sort(a_copy, new_list, 0, len(a)-1)


def merge_sort(a, new_a, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += merge_sort(a, new_a, left, mid)
        count += merge_sort(a, new_a, mid+1, right)
        count += merge(a, new_a, left, mid, right)
    return count


def merge(a, new_a, left, mid, right):
    i = k = left
    j = mid + 1
    count = 0

    while i <= mid and j <= right:
        if a[i] <= a[j]:
            new_a[k] = a[i]
            k += 1
            i += 1
        else:
            new_a[k] = a[j]
            count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        new_a[k] = a[i]
        k += 1
        i += 1

    while j <= right:
        new_a[k] = a[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        a[loop_var] = new_a[loop_var]

    return count


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))

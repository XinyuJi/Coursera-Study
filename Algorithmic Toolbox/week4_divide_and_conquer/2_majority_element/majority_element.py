# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def find_majority(elements):
    count, num = 0, 0
    for e in elements:
        if e == num:
            count += 1
        elif count == 0:
            count, num = 1, e
        else:
            count -= 1
    return num


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    nums = elements[:]
    if len(nums) == 1:
        return nums[0]
    a = find_majority(nums[0: len(nums)//2])
    b = find_majority(elements[len(nums)//2:len(nums)])
    if elements.count(a) > len(nums)/2 or elements.count(b) > len(nums)/2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))

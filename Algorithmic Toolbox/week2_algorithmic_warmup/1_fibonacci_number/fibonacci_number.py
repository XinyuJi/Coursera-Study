# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n

    i = 0
    nums = [0, 1]
    while i < n-1:
        nums.append(nums[-1]+nums[-2])
        i += 1

    return nums[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

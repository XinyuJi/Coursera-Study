# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n % 10

    i = 0
    nums = [0, 1]
    while i < n-1:
        nums.append((nums[-1]+nums[-2]) % 10)
        i += 1

    return nums[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))

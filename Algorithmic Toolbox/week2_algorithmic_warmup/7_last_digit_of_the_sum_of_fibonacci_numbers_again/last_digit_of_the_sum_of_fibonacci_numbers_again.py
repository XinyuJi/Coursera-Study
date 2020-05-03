# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    start = from_index % 60
    diff = (to_index - from_index) % 60
    end = start + diff

    fibonacci_numbers = [0, 1]
    for i in range(2, 60):
        fibonacci_numbers.append((fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]) % 10)

    if end <= 60:
        return sum(fibonacci_numbers[start:(end+1)]) % 10
    else:
        return (sum(fibonacci_numbers[start:60]) + sum(fibonacci_numbers[0:(start+diff-60+1)])) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))

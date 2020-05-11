# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    number_list = numbers[:]
    largest = []
    while len(number_list) > 0:
        put_ahead = '0'
        for number in number_list:
            if str(number) + put_ahead > put_ahead + str(number):
                put_ahead = str(number)
                put_num = number
        largest.append(put_ahead)
        number_list.remove(put_num)
    return int("".join(largest))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))

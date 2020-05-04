# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)
    value = 0
    max_index = 0
    rate = [a / b for a, b in zip(prices, weights)]
    while capacity > 0 and rate:
        max_index = rate.index(max(rate))
        a = min(capacity, weights[max_index])
        value += a * max(rate)
        capacity -= a
        if a == weights[max_index]:
            rate.remove(max(rate))
            del weights[max_index]

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

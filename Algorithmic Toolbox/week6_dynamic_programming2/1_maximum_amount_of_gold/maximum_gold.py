# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    DP = [[0 for j in range(capacity+1)] for i in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            DP[i][j] = DP[i-1][j]
            if weights[i-1] <= j:
                val = DP[i-1][j - weights[i-1]] + weights[i-1]
                if val > DP[i][j]:
                    DP[i][j] = val
    return DP[-1][-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

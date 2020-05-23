# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    x = len(first_sequence)
    y = len(second_sequence)
    DP = [[0] * (y+1) for k in range(x+1)]

    for i in range(x):
        for j in range(y):
            if first_sequence[i] == second_sequence[j]:
                DP[i+1][j+1] = DP[i][j] + 1
            else:
                DP[i+1][j+1] = max(DP[i+1][j], DP[i][j+1])
    return DP[-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))

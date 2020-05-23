# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    x = len(first_sequence)
    y = len(second_sequence)
    z = len(third_sequence)
    DP = [[[0 for z1 in range(z+1)] for y1 in range(y+1)] for x1 in range(x+1)]

    for i in range(1, x+1):
        for j in range(1, y+1):
            for k in range(1, z+1):
                if first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1]:
                    DP[i][j][k] = DP[i-1][j-1][k-1] + 1
                else:
                    DP[i][j][k] = max(DP[i-1][j][k], DP[i][j-1][k], DP[i][j][k-1])
    return DP[-1][-1][-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

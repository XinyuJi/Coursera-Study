# python3


def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    DP = [[j for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        DP[i][0] = i

    for i in range(1,m+1):
        for j in range(1, n+1):
            if first_string[i-1] == second_string[j-1]:
                DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, DP[i-1][j-1])
            else:
                DP[i][j] = min(DP[i-1][j]+1, DP[i][j-1]+1, DP[i-1][j-1]+1)
    return  DP[-1][-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

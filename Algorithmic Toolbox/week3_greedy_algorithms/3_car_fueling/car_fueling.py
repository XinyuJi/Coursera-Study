# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    if d <= m:
        return 0

    count = 0
    stops.append(d)
    for i in range(1, len(stops)):
        if stops[i] - stops[i-1] > m:
            return -1

    i = 1
    start = 0
    while i <= len(stops)-1:
        if stops[i - 1] - start <= m < stops[i] - start:
            start = stops[i-1]
            count = count + 1
        i = i + 1
    return count


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))

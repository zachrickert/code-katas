def series_sum(n):
    if n == 0:
        return 0
    sum = 0
    for i in range(n):
        sum += 1 / ((3 * i) + 1)
    return '{:.2f}'.format(sum)


print(series_sum(1))
print(series_sum(2))
print(series_sum(3))
print(series_sum(0))

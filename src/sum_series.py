"""Code for codewars.  Sum of Nth series."""


def series_sum(n):
    """Print the sum of the series 1 /(3N +1)."""
    if n == 0:
        return '{:.2f}'.format(0)
    sum_of_series = 0.0
    for i in range(n):
        sum_of_series += 1.0 / ((3 * i) + 1)
    return '{:.2f}'.format(sum_of_series)

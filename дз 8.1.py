def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end))

print(sum_range(start,end))

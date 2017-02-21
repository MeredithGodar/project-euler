def multiples_of_3_and_5(max_range):
    total = 0

    for x in range(1, max_range, 1):
        if x % 3 == 0 or x % 5 == 0:
            total += x

    return total

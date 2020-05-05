def isPerfect(n):
    return (n ** 0.5).is_integer()


def find_next_square(sq):
    if isPerfect(sq):
        x = sq + 1
        while not isPerfect(x):
            x += 1
        return x
    else:
        return -1
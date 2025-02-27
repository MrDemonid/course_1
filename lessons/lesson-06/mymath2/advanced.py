def exp_int(n: int, e: int) -> int:
    while e > 0:
        n *= n;
        e -= 1
    return n

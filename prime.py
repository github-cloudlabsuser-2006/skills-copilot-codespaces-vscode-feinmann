def prime():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1
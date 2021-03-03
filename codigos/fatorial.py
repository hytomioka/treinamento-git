def fatorial(n):
    if (n == 1):
        return n
    return fatorial(n-1) * n

print(fatorial(6))
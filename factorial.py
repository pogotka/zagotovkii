num = 5

def factorial(n):
    if n == 0:
        return 1
    f = 1
    i = 0

    while i < n:
        i += 1
        f = f * i
    return f

print("факториал числа {n} равен {f}".format(n=num, f=factorial(num)))
a = float(input())
n = int(input())
def mult_func(a, n):
    if n == 0:
        return 1
    else:
        return a * mult_func(a, n - 1)

print(mult_func(a, n))
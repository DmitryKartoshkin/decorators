from decorator import timer
@timer
def factorial(n):
    fact = 1
    for f in range(1, n+1):
        fact *= f
    return fact

if __name__ == "__main__":
    f_5 = factorial(5)
    f_ = factorial(f_5)
    # factorial(100)
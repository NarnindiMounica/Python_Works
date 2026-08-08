def fib_series(number):
    if number <= 1:
        return 1
    else:
        return fib_series(number-1) + fib_series(number-2)
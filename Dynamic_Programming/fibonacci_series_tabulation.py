def fib_series_bottom_up(number):
    dp = [0] * (number + 1)

    dp[0] = 0
    dp [1] = 1
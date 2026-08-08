num_dict= {}
def fib_series_with_calls(number):
    
    if number not in num_dict.keys():
        num_dict[number] = 1
    else:
        num_dict[number] += 1 

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        fib_n1 =  fib_series_with_calls(number-1)
        fib_n2 = fib_series_with_calls(number-2)   

        fib_n = fib_n1 + fib_n2
        
    return fib_n


def fib_series(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib_series(number-1) + fib_series(number-2)

dairy_num = [-1] * (9)
def fib_series_with_dp(number):

    if dairy_num[number] != -1:
        return dairy_num[number]

    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        dairy_num[number-1] = fib_series_with_dp(number-1)
        dairy_num[number-2] = fib_series_with_dp(number-2)

        dairy_num[number] = dairy_num[number-1] + dairy_num[number-2]

        return dairy_num[number]

print(fib_series_with_dp(8))


# print(fib_series_with_calls(5))
# print(num_dict) 


# fib_series(number=5)

    
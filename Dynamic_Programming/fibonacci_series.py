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


print(fib_series_with_calls(5))
print(num_dict) 


fib_series(number=5)

    
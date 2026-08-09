def min_steps_to_one(number):

    if number == 1:
        return 0
    
    steps = min_steps_to_one(number-1)+1

    
    if number % 2 == 0:
        steps = min(steps, min_steps_to_one(number//2))+1

    
    if number % 3 == 0:
        steps = min(steps, min_steps_to_one(number//3))+1

    return steps    

print(min_steps_to_one(7))


def min_steps_to_one_dp(number, memo):

    if number == 1:
        return 0

    if memo[number] != -1:
        return memo[number]
     
    steps = min_steps_to_one_dp(number-1, memo)+1

    if number % 2 == 0:
        steps = min(steps, min_steps_to_one_dp(number//2, memo))+1

    if number % 3 == 0:
        steps = min(steps, min_steps_to_one_dp(number//3, memo))+1

    memo[number] = steps
    return memo[number]    

number = 7
memo = [-1] * (number + 1)
print(min_steps_to_one_dp(number, memo))
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

def min_steps_to_one_tab(number, dp):

    dp[1] = 0

    for i in range(2, number+1):
        ans = dp[i-1]+1

        if i%2 == 0:
            ans = min(ans, dp[i//2]+1)

        if i%3 == 0:
            ans = min(ans, dp[i//3]+1)

        dp[i] = ans       
    return dp[number]    

number = 9
dp = [0] * (number + 1)
print(min_steps_to_one_tab(number, dp))        


    
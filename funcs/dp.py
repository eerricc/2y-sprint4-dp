from datetime import datetime

def exp_top(lista):
    dates = [datetime.strptime(item["validade"], "%d/%m/%Y") for item in lista]
    memo = {}
    def lis(idx, prev_dt):
        key = (idx, prev_dt)
        if key in memo:
            return memo[key]
        if idx == len(dates):
            return 0
        skip = lis(idx + 1, prev_dt)
        take = 0
        if prev_dt is None or dates[idx] > prev_dt:
            take = 1 + lis(idx + 1, dates[idx])
        memo[key] = max(skip, take)
        return memo[key]
    return lis(0, None)

def exp_bot(lista):
    dates = [datetime.strptime(item["validade"], "%d/%m/%Y") for item in lista]
    n = len(dates)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if dates[i] > dates[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
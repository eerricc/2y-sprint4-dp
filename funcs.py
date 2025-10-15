from datetime import datetime
import time
import tracemalloc
import random

# dummy medical items
consumos = [

]

random.shuffle(consumos)

def register():
    while True:
        try:
            # get name
            while True:
                nome = input("item name: ").strip()
                if nome: 
                    break
                print("type a name: ")

            # get quantity
            while True:
                qtd_str = input("item quantity: ")
                if qtd_str.isdigit() and int(qtd_str) > 0:
                    quantidade = int(qtd_str)
                    break
                print("-> quantity must be a positive number")

            # get expiration date
            while True:
                validade = input("expiration date (dd/mm/yyyy): ").strip()
                try:
                    datetime.strptime(validade, "%d/%m/%Y")  # format
                    break
                except ValueError:
                    print("-> invalid date format")

            # cost per unit
            while True:
                cos = input("cost per unit: ")
                if cos.isdigit() and int(cos) > 0:
                    cost = int(cos)
                    break
                print("-> cost must be a positive number")
            
            # batch size
            while True:
                bat = input("batch size: ")
                if bat.isdigit() and int(bat) > 0:
                    batch = int(bat)
                    break
                print("-> batch size must be a positive number")

            consumos.append({
                "name": nome,
                "quantity": quantidade,
                "validade": validade,
                "cost/unit": cost,
                "batch": batch
            })

            print("-> success\n")
            return

        except KeyboardInterrupt:
            print("\n-> stopping.")
            break

def edit():
    pass

def searcha():
    pass

def check():
    for i in sorted(consumos, key=lambda x: datetime.strptime(x["validade"], "%d/%m/%Y")):
        print(i)

def exp_top():
    dates = [datetime.strptime(item["validade"], "%d/%m/%Y") for item in consumos]
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

def exp_bot():
    dates = [datetime.strptime(item["validade"], "%d/%m/%Y") for item in consumos]
    n = len(dates)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if dates[i] > dates[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)





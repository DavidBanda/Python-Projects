# 25(quarter) 10(dime) 5(nickel) 1(pennies)
# 78


def num_coins(cents, no_coin):
    dict_coins = {"quarter": [25, 0], "dime": [10, 0], "nickel": [5, 0], "penny": [1, 0]}
    name_coins = ["quarter", "dime", "nickel", "penny"]
    ct = []

    if no_coin != "":
        dict_coins.pop(no_coin)
        name_coins.pop(name_coins.index(no_coin))

    for i in range(len(name_coins) - 1):
        name_coins[0], name_coins[i] = name_coins[i], name_coins[0]
        ct.append(evaluate(cents, dict_coins, name_coins))
    print(ct)


def evaluate(cents, dict_coins, name_coins):
    coins = 0
    for i in range(len(dict_coins)):
        while True:
            if cents - dict_coins[name_coins[i]][0] >= 0:
                dict_coins[name_coins[i]][1] = dict_coins[name_coins[i]][1] + 1
                cents -= dict_coins[name_coins[i]][0]
            else:
                coins += dict_coins[name_coins[i]][1]
                print(f'{name_coins[i]}({dict_coins[name_coins[i]][0]}): {dict_coins[name_coins[i]][1]}')
                break
        continue
    print()
    return coins


num_coins(71, "")






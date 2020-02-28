def change_coin(pay, cost):
    change = round(pay - cost, 2)
    print(change)

    print(f'Quarter (.25): {change // .25}')
    change = round(change % .25, 2)

    print(f'Dime (.10): {change // .10}')
    change = round(change % .10, 2)

    print(f'Nickel (.05): {change // .05}')
    change = round(change % .05, 2)

    print(f'Penny (.01): {change * 100}')


change_coin(1, .11)



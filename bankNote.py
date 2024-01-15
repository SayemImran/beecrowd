rcved_money = int(input())
curent_money=rcved_money
remaining = 0
counter_100 = 0
counter_50= 0
counter_20 = 0
counter_10 = 0
counter_5 = 0
counter_2 = 0
counter_1 = 0


if curent_money % 100 < 100:
    counter_100 = curent_money // 100
    remaining = curent_money % 100
    if remaining % 50 < 50:
        counter_50 = remaining // 50
        remaining = remaining % 50
        if remaining % 20 < 20:
            counter_20 = remaining // 20
            remaining = remaining % 20
            if remaining % 10 < 10:
                counter_10 = remaining // 10
                remaining = remaining % 10
                if remaining % 5 < 5:
                    counter_5 = remaining // 5
                    remaining = remaining % 5
                    if remaining % 2 < 2:
                        counter_2 = remaining // 2
                        remaining = remaining % 2
                        counter_1 = remaining
                    else:
                        print("In sufficient ballance")


print(f"{counter_100} nota(s) de R$ 100,00")
print(f"{counter_50} nota(s) de R$ 50,00")
print(f"{counter_20} nota(s) de R$ 20,00")
print(f"{counter_10} nota(s) de R$ 10,00")
print(f"{counter_5} nota(s) de R$ 5,00")
print(f"{counter_2} nota(s) de R$ 2,00")
print(f"{counter_1} nota(s) de R$ 1,00")

from pprint import pprint
from collections import Counter
import time


coins_rub = [
    {"nominal": 5000, "count": 100},
    {"nominal": 1000, "count": 100},
    {"nominal": 500, "count": 100},
    {"nominal": 100, "count": 100},
    {"nominal": 50, "count": 100},
    {"nominal": 10, "count": 100},
    {"nominal": 5, "count": 100},
    {"nominal": 1, "count": 1}
]

balance_rub = []
for i in coins_rub:
    res_rub = 1
    for key in i:
        res_rub = res_rub * i[key]
    balance_rub.append(res_rub)
balance_rub = sum(balance_rub)

lw_rub = [1]

coins_usd = [
    {"nominal": 5000, "count": 50},
    {"nominal": 1000, "count": 50},
    {"nominal": 500, "count": 50},
    {"nominal": 100, "count": 50},
    {"nominal": 50, "count": 50},
    {"nominal": 10, "count": 50},
    {"nominal": 5, "count": 50},
    {"nominal": 1, "count": 50}
]

balance_usd = []
for i in coins_usd:
    res_usd = 1
    for key in i:
        res_usd = res_usd * i[key]
    balance_usd.append(res_usd)
balance_usd = sum(balance_usd)

lw_usd = [1]

coins_eur = [
    {"nominal": 5000, "count": 10},
    {"nominal": 1000, "count": 10},
    {"nominal": 500, "count": 10},
    {"nominal": 100, "count": 10},
    {"nominal": 50, "count": 10},
    {"nominal": 10, "count": 10},
    {"nominal": 5, "count": 10},
    {"nominal": 1, "count": 10}
]

balance_eur = []
for i in coins_eur:
    res_eur = 1
    for key in i:
        res_eur = res_eur * i[key]
    balance_eur.append(res_eur)
balance_eur = sum(balance_eur)

lw_eur = [1]


class ATM:
    def __init__(self, coins_rub, balance_rub, lw_rub, coins_usd, balance_usd, lw_usd, coins_eur, balance_eur, lw_eur):
        self.coins_rub = coins_rub
        self.balance_rub = balance_rub
        self.lw_rub = lw_rub
        self.coins_usd = coins_usd
        self.balance_usd = balance_usd
        self.lw_usd = lw_usd
        self.coins_eur = coins_eur
        self.balance_eur = balance_eur
        self.lw_eur = lw_eur

    def sleep(func):
        def wrap(*args, **kwargs):
            time.sleep(1)
            func(*args, **kwargs)
        return wrap

    def get_rub(self, amount, coinindex=0):
        # time.sleep(3)
        if amount == 0:
            return []
        elif amount > self.balance_rub:
            return
        if coinindex >= len(self.coins_rub):
            return None
        coin = self.coins_rub[coinindex]
        coinindex += 1
        canTake = min(amount // coin["nominal"], coin["count"])
        self.lw_rub.append(canTake)
        for count in range(canTake, -1, -1):
            change = obj.get_rub(amount - coin["nominal"] * count, coinindex)
            if change is not None:
                if count:
                    return change + [{"nominal": coin["nominal"], "count": count}]
                return change

    def get_usd(self, amount, coinindex=0):
        # time.sleep(3)
        if amount == 0:
            return []
        elif amount > self.balance_usd:
            return
        if coinindex >= len(self.coins_usd):
            return None
        coin = self.coins_usd[coinindex]
        coinindex += 1
        canTake = min(amount // coin["nominal"], coin["count"])
        self.lw_usd.append(canTake)
        for count in range(canTake, -1, -1):
            change = obj.get_usd(amount - coin["nominal"] * count, coinindex)
            if change is not None:
                if count:
                    return change + [{"nominal": coin["nominal"], "count": count}]
                return change

    def get_eur(self, amount, coinindex=0):
        # time.sleep(3)
        if amount == 0:
            return []
        elif amount > self.balance_eur:
            return
        if coinindex >= len(self.coins_eur):
            return None
        coin = self.coins_eur[coinindex]
        coinindex += 1
        canTake = min(amount // coin["nominal"], coin["count"])
        self.lw_eur.append(canTake)
        for count in range(canTake, -1, -1):
            change = obj.get_eur(amount - coin["nominal"] * count, coinindex)
            if change is not None:
                if count:
                    return change + [{"nominal": coin["nominal"], "count": count}]
                return change

    def bank_minus_withd_rub(self):
        l_coins = []
        for i in self.coins_rub:
            for value in i.values():
                l_coins.append(value)
        l_coins_keys = l_coins[::2]
        l_coins_values = l_coins[1::2]
        l_tup_coins = dict(zip(l_coins_keys, l_coins_values))
        l_withd = []
        for i in answer_rub:
            for value in i.values():
                l_withd.append(value)
        l_withd_keys = l_withd[::2]
        l_withd_values = l_withd[1::2]
        l_tup_withd = dict(zip(l_withd_keys, l_withd_values))
        bank = Counter(l_tup_coins)
        withd = Counter(l_tup_withd)
        bank.subtract(withd)
        d = dict(bank)
        # print(l_tup_coins)
        # print(l_tup_withd)
        # print(d)
        l_remainder = []
        for value in d.values():
            if value < 0:
                l_remainder.append(0)
            else:
                l_remainder.append(value)
        # print(l_remainder)

        self.coins_rub = [
            {"nominal": 5000, "count": l_remainder[0]},
            {"nominal": 1000, "count": l_remainder[1]},
            {"nominal": 500, "count": l_remainder[2]},
            {"nominal": 100, "count": l_remainder[3]},
            {"nominal": 50, "count": l_remainder[4]},
            {"nominal": 10, "count": l_remainder[5]},
            {"nominal": 5, "count": l_remainder[6]},
            {"nominal": 1, "count": l_remainder[7]}
        ]

        self.balance_rub = []
        for i in self.coins_rub:
            res_rub = 1
            for key in i:
                res_rub = res_rub * i[key]
            obj.balance_rub.append(res_rub)
        self.balance_rub = sum(self.balance_rub)

        return self.balance_rub, self.coins_rub

    def bank_minus_withd_usd(self):
        l_coins = []
        for i in self.coins_usd:
            for value in i.values():
                l_coins.append(value)
        l_coins_keys = l_coins[::2]
        l_coins_values = l_coins[1::2]
        l_tup_coins = dict(zip(l_coins_keys, l_coins_values))
        l_withd = []
        for i in answer_usd:
            for value in i.values():
                l_withd.append(value)
        l_withd_keys = l_withd[::2]
        l_withd_values = l_withd[1::2]
        l_tup_withd = dict(zip(l_withd_keys, l_withd_values))
        bank = Counter(l_tup_coins)
        withd = Counter(l_tup_withd)
        bank.subtract(withd)
        d = dict(bank)
        # print(l_tup_coins)
        # print(l_tup_withd)
        # print(d)
        l_remainder = []
        for value in d.values():
            if value < 0:
                l_remainder.append(0)
            else:
                l_remainder.append(value)
        # print(l_remainder)

        self.coins_usd = [
            {"nominal": 5000, "count": l_remainder[0]},
            {"nominal": 1000, "count": l_remainder[1]},
            {"nominal": 500, "count": l_remainder[2]},
            {"nominal": 100, "count": l_remainder[3]},
            {"nominal": 50, "count": l_remainder[4]},
            {"nominal": 10, "count": l_remainder[5]},
            {"nominal": 5, "count": l_remainder[6]},
            {"nominal": 1, "count": l_remainder[7]}
        ]

        self.balance_usd = []
        for i in self.coins_usd:
            res_usd = 1
            for key in i:
                res_usd = res_usd * i[key]
            obj.balance_usd.append(res_usd)
        self.balance_usd = sum(self.balance_usd)

        return self.balance_usd, self.coins_usd

    def bank_minus_withd_eur(self):
        l_coins = []
        for i in self.coins_eur:
            for value in i.values():
                l_coins.append(value)
        l_coins_keys = l_coins[::2]
        l_coins_values = l_coins[1::2]
        l_tup_coins = dict(zip(l_coins_keys, l_coins_values))
        l_withd = []
        for i in answer_eur:
            for value in i.values():
                l_withd.append(value)
        l_withd_keys = l_withd[::2]
        l_withd_values = l_withd[1::2]
        l_tup_withd = dict(zip(l_withd_keys, l_withd_values))
        bank = Counter(l_tup_coins)
        withd = Counter(l_tup_withd)
        bank.subtract(withd)
        d = dict(bank)
        # print(l_tup_coins)
        # print(l_tup_withd)
        # print(d)
        l_remainder = []
        for value in d.values():
            if value < 0:
                l_remainder.append(0)
            else:
                l_remainder.append(value)
        # print(l_remainder)

        self.coins_eur = [
            {"nominal": 5000, "count": l_remainder[0]},
            {"nominal": 1000, "count": l_remainder[1]},
            {"nominal": 500, "count": l_remainder[2]},
            {"nominal": 100, "count": l_remainder[3]},
            {"nominal": 50, "count": l_remainder[4]},
            {"nominal": 10, "count": l_remainder[5]},
            {"nominal": 5, "count": l_remainder[6]},
            {"nominal": 1, "count": l_remainder[7]}
        ]

        self.balance_eur = []
        for i in self.coins_eur:
            res_eur = 1
            for key in i:
                res = res_eur * i[key]
            obj.balance_eur.append(res_eur)
        self.balance_eur = sum(self.balance_eur)

        return self.balance_eur, self.coins_eur

    @sleep
    def deposit(self, currency_deposit, five_th, one_th, f_hun, one_hun, fifty, ten, five, one_1):

        if currency_deposit == 1:

            five_th_new = []
            ft = self.coins_rub[0]
            for i in ft.values():
                five_th_new.append(i + five_th)
            five_th_new = five_th_new[1]

            one_th_new = []
            ot = self.coins_rub[1]
            for i in ot.values():
                one_th_new.append(i + one_th)
            one_th_new = one_th_new[1]

            f_hun_new = []
            fh = self.coins_rub[2]
            for i in fh.values():
                f_hun_new.append(i + f_hun)
            f_hun_new = f_hun_new[1]

            one_hun_new = []
            on = self.coins_rub[3]
            for i in on.values():
                one_hun_new.append(i + one_hun)
            one_hun_new = one_hun_new[1]

            fifty_new = []
            fy = self.coins_rub[4]
            for i in fy.values():
                fifty_new.append(i + fifty)
            fifty_new = fifty_new[1]

            ten_new = []
            t = self.coins_rub[5]
            for i in t.values():
                ten_new.append(i + ten)
            ten_new = ten_new[1]

            five_new = []
            f = self.coins_rub[6]
            for i in f.values():
                five_new.append(i + five)
            five_new = five_new[1]

            one_new = []
            o = self.coins_rub[7]
            for i in o.values():
                one_new.append(i + one_1)
            one_new = one_new[1]

            self.coins_rub = [
                {"nominal": 5000, "count": five_th_new},
                {"nominal": 1000, "count": one_th_new},
                {"nominal": 500, "count": f_hun_new},
                {"nominal": 100, "count": one_hun_new},
                {"nominal": 50, "count": fifty_new},
                {"nominal": 10, "count": ten_new},
                {"nominal": 5, "count": five_new},
                {"nominal": 1, "count": one_new}
            ]

            self.balance_rub = []
            for i in self.coins_rub:
                self.res_rub = 1
                for key in i:
                    self.res_rub = self.res_rub * i[key]
                obj.balance_rub.append(self.res_rub)
            self.balance_rub = sum(self.balance_rub)

            return self.balance_rub, self.coins_rub

        elif currency_deposit == 2:

            five_th_new = []
            ft = self.coins_usd[0]
            for i in ft.values():
                five_th_new.append(i + five_th)
            five_th_new = five_th_new[1]

            one_th_new = []
            ot = self.coins_usd[1]
            for i in ot.values():
                one_th_new.append(i + one_th)
            one_th_new = one_th_new[1]

            f_hun_new = []
            fh = self.coins_usd[2]
            for i in fh.values():
                f_hun_new.append(i + f_hun)
            f_hun_new = f_hun_new[1]

            one_hun_new = []
            on = self.coins_usd[3]
            for i in on.values():
                one_hun_new.append(i + one_hun)
            one_hun_new = one_hun_new[1]

            fifty_new = []
            fy = self.coins_usd[4]
            for i in fy.values():
                fifty_new.append(i + fifty)
            fifty_new = fifty_new[1]

            ten_new = []
            t = self.coins_usd[5]
            for i in t.values():
                ten_new.append(i + ten)
            ten_new = ten_new[1]

            five_new = []
            f = self.coins_usd[6]
            for i in f.values():
                five_new.append(i + five)
            five_new = five_new[1]

            one_new = []
            o = self.coins_usd[7]
            for i in o.values():
                one_new.append(i + one_1)
            one_new = one_new[1]

            self.coins_usd = [
                {"nominal": 5000, "count": five_th_new},
                {"nominal": 1000, "count": one_th_new},
                {"nominal": 500, "count": f_hun_new},
                {"nominal": 100, "count": one_hun_new},
                {"nominal": 50, "count": fifty_new},
                {"nominal": 10, "count": ten_new},
                {"nominal": 5, "count": five_new},
                {"nominal": 1, "count": one_new}
            ]

            self.balance_usd = []
            for i in self.coins_usd:
                self.res_usd = 1
                for key in i:
                    self.res_usd = self.res_usd * i[key]
                obj.balance_usd.append(self.res_usd)
            self.balance_usd = sum(self.balance_usd)

            return self.balance_usd, self.coins_usd

        else:
            five_th_new = []
            ft = self.coins_eur[0]
            for i in ft.values():
                five_th_new.append(i + five_th)
            five_th_new = five_th_new[1]

            one_th_new = []
            ot = self.coins_eur[1]
            for i in ot.values():
                one_th_new.append(i + one_th)
            one_th_new = one_th_new[1]

            f_hun_new = []
            fh = self.coins_eur[2]
            for i in fh.values():
                f_hun_new.append(i + f_hun)
            f_hun_new = f_hun_new[1]

            one_hun_new = []
            on = self.coins_eur[3]
            for i in on.values():
                one_hun_new.append(i + one_hun)
            one_hun_new = one_hun_new[1]

            fifty_new = []
            fy = self.coins_eur[4]
            for i in fy.values():
                fifty_new.append(i + fifty)
            fifty_new = fifty_new[1]

            ten_new = []
            t = self.coins_eur[5]
            for i in t.values():
                ten_new.append(i + ten)
            ten_new = ten_new[1]

            five_new = []
            f = self.coins_eur[6]
            for i in f.values():
                five_new.append(i + five)
            five_new = five_new[1]

            one_new = []
            o = self.coins_eur[7]
            for i in o.values():
                one_new.append(i + one_1)
            one_new = one_new[1]

            self.coins_eur = [
                {"nominal": 5000, "count": five_th_new},
                {"nominal": 1000, "count": one_th_new},
                {"nominal": 500, "count": f_hun_new},
                {"nominal": 100, "count": one_hun_new},
                {"nominal": 50, "count": fifty_new},
                {"nominal": 10, "count": ten_new},
                {"nominal": 5, "count": five_new},
                {"nominal": 1, "count": one_new}
            ]

            self.balance_eur = []
            for i in self.coins_eur:
                self.res_eur = 1
                for key in i:
                    self.res_eur = self.res_eur * i[key]
                obj.balance_eur.append(self.res_eur)
            self.balance_eur = sum(self.balance_eur)

            return self.balance_eur, self.coins_eur

    @sleep
    def your_balance(self, currency):
        if currency == 1:
            balance = obj.balance_rub
            coins = obj.coins_rub
            a = "рублевом"
        elif currency == 2:
            balance = obj.balance_usd
            coins = obj.coins_usd
            a = "долларовом"
        else:
            balance = obj.balance_eur
            coins = obj.coins_eur
            a = "евровом"
        pprint(f'{coins}')
        print(f'На вашем {a} счете, {balance}')


obj = ATM(coins_rub, balance_rub, lw_rub, coins_usd, balance_usd, lw_usd, coins_eur, balance_eur, lw_eur)


while True:
    time.sleep(1)
    print("Menu:")
    print("1. Balance check")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    ch = input("Enter your choice:")
    if ch == '1':
        time.sleep(1)
        print("Чтобы проверить ваш рублёвый счет, введите 1:")
        print("Чтобы проверить ваш долларовый счет, введите 2:")
        print("Чтобы проверить ваш евровый счет, введите 3:")
        while True:
            try:
                currency = int(input("Enter your choice:"))
                if 0 < currency < 4:
                    break
            except ValueError:
                print("Введите целое число от 1 до 3!")
#
        obj.your_balance(currency)

    elif ch == '2':
        print("Чтобы внести деньги ваш рублёвый счет, введите 1:")
        print("Чтобы внести деньги ваш долларовый счет, введите 2:")
        print("Чтобы внести деньги ваш евровый счет, введите 3:")
        while True:
            try:
                currency_deposit = int(input("Enter your choice:"))
                if 0 < currency_deposit < 4:
                    break
            except ValueError:
                print("Введите целое число от 1 до 3!")
        while True:
            try:
                five_th = int(input("Количество вносимых банкнот номиналом [5000] от 1 до 2500:"))
                if 0 <= five_th < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")
        while True:
            try:
                one_th = int(input("Количество вносимых банкнот номиналом [1000] от 1 до 2500:"))
                if 0 <= one_th < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")

        while True:
            try:
                f_hun = int(input("Количество вносимых банкнот номиналом [500] от 1 до 2500:"))
                if 0 <= f_hun < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")
        while True:
            try:
                one_hun = int(input("Количество вносимых банкнот номиналом [100] от 1 до 2500:"))
                if 0 <= one_hun < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")
        while True:
            try:
                fifty = int(input("Количество вносимых банкнот номиналом [50] от 1 до 2500:"))
                if 0 <= fifty < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")

        while True:
            try:
                ten = int(input("Количество вносимых банкнот номиналом [10] от 1 до 2500:"))
                if 0 <= ten < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")

        while True:
            try:
                five = int(input("Количество вносимых банкнот номиналом [5] от 1 до 2500:"))
                if 0 <= five < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")

        while True:
            try:
                one_1 = int(input("Количество вносимых банкнот номиналом [1] от 1 до 2500:"))
                if 0 <= one_1 < 2501:
                    break
            except ValueError:
                print("Введите целое число от 1 до 2500!")

        obj.deposit(currency_deposit, five_th, one_th, f_hun, one_hun, fifty, ten, five, one_1)

    elif ch == '3':
        print("Чтобы снять деньги с вашего рублёвого счета, введите 1:")
        print("Чтобы снять деньги с вашего долларового счета, введите 2:")
        print("Чтобы снять деньги с вашего еврового счета, введите 3:")
        while True:
            try:
                currency_withdraw = int(input("Enter your choice:"))
                if 0 < currency_withdraw < 4:
                    break
            except ValueError:
                print("Введите целое число от 1 до 3!")
        if currency_withdraw == 1:
            while True:
                try:
                    a = int(input("Enter the amount:"))
                    if 0 < a < obj.balance_rub:
                        try:
                            obj.get_rub(a)
                            answer_rub = obj.get_rub(a)
                            break
                        except ValueError:
                            print(f"Максимальная сумма для снятия равна {obj.balance_rub}")
                    elif a > obj.balance_rub:
                        print(f"Максимальная сумма для снятия равна {obj.balance_rub}")
                        continue
                except ValueError:
                    print(f"Введите число! Максимальная сумма для снятия равна {obj.balance_rub}")
            if answer_rub is not None:
                print(answer_rub)
                bank_minus_withd = obj.bank_minus_withd_rub()
            else:
                print("Недостаточный баланс или невозможно выдать деньги")
        elif currency_withdraw == 2:
            while True:
                try:
                    a = int(input("Enter the amount:"))
                    if 0 < a < obj.balance_usd:
                        try:
                            obj.get_usd(a)
                            answer_usd = obj.get_usd(a)
                            break
                        except ValueError:
                            print(f"Максимальная сумма для снятия равна {obj.balance_usd}")
                    elif a > obj.balance_rub:
                        print(f"Максимальная сумма для снятия равна {obj.balance_rub}")
                        continue
                except ValueError:
                    print(f"Введите число! Максимальная сумма для снятия равна {obj.balance_usd}")
            if answer_usd is not None:
                print(answer_usd)
                bank_minus_withd_usd = obj.bank_minus_withd_usd()
            else:
                print("Недостаточный баланс или невозможно выдать деньги")
        else:
            while True:
                try:
                    a = int(input("Enter the amount:"))
                    if 0 < a < obj.balance_eur:
                        try:
                            obj.get_eur(a)
                            answer_eur = obj.get_eur(a)
                            break
                        except ValueError:
                            print(f"Максимальная сумма для снятия равна {obj.balance_eur}")
                    elif a > obj.balance_rub:
                        print(f"Максимальная сумма для снятия равна {obj.balance_rub}")
                        continue
                except ValueError:
                    print(f"Введите число! Максимальная сумма для снятия равна {obj.balance_eur}")
            if answer_eur is not None:
                print(answer_eur)
                bank_minus_withd_eur = obj.bank_minus_withd_eur()
            else:
                print("Недостаточный баланс или невозможно выдать деньги")
    elif ch == '4':
        print("Thank you.. visit again..")
    else:
        if ch != '1' or ch != '2' or ch != '3' or ch != '4':
            print("Введите число от 1 до 4")
            continue
    time.sleep(1)

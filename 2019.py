class employee:
    table = {36000: [0.03, 0], 144000: [0.1, 2520], 300000: [0.2, 16920],
             420000: [0.25, 31920], 660000: [0.3, 52920], 960000: [0.35, 85920],
             10000000: [0.45, 181920]}
    bonus = {13: 3000, 14: 4000}
    nIncome = []
    nTax = []

    def caltax(self, y):
        ll = [0, 0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
        ss = [0, 0, 210, 1410, 2660, 4410, 7160, 14360]
        xx = [-5000, 0, 3000, 12000, 25000, 35000, 55000, 80000, 1000000]
        xx = list(map(lambda n:n+5000, xx))
        for i in range(len(xx) - 1):
            if y > xx[i] and y < xx[i + 1]:
                return (y - 5000) * ll[i] - ss[i]

    def __init__(self, baseIncome, grade=14, flag="Before"):
        if flag == "Before":
            extra = 0
            hb = 0.12
        else:
            extra = 0
            hb = 0.05
        houseBounding = baseIncome * hb * 2
        mExtra = baseIncome / 21.75 * 2
        realIncome = baseIncome + self.bonus[grade] + mExtra
        tax = 0
        for n in range(1, 13):
            income = n * (realIncome - baseIncome * (0.105 + hb))
            incomeForTax = income - n * 5000
            for t in self.table:
                if incomeForTax < t:
                    tax = incomeForTax * self.table[t][0] - self.table[t][1] - sum(self.nTax)
                    break
            # print(income)
            print(tax)
            self.nIncome.append(income)
            self.nTax.append(tax)
        yHouseBounding = 12 * houseBounding
        yBonus = 3 * (baseIncome + self.bonus[grade]) - self.caltax(3 * (baseIncome + self.bonus[grade]))
        yExtra = 12 * baseIncome / 21.75 * 2 - self.caltax(12 * baseIncome / 21.75 * 2)
        yTotal = self.nIncome.pop() + yHouseBounding + yBonus + yExtra
        print(yTotal)

class employee_new:
    table_1 = [0, 36000, 144000, 300000, 420000, 660000, 960000, float("inf")]
    table_2 = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
    table_3 = [0, 2520, 16920, 31920, 52920, 85920, 181920]
    def __init__(self, base = 12000, bonus = 4000, extraday = 1, final = 3):
        self.income = 12 * (base + bonus + base * 0.24 + (extraday + 1) * base / 21.75 * 2) + final * (base + bonus)
        for i in range(len(self.table_1) - 1):
            if (self.income - 60000) < self.table_1[i]:
                print(i)
                self.tax = (self.income - 60000) * self.table_2[i - 1] - self.table_3[i - 1]
                self.real = self.income - self.tax
                break
# Gry = employee(12000)

Gry = employee_new()
print(Gry.income)
print(Gry.tax)
print(Gry.real)
class Income:
    # ll: 利率 ss: 速算差额 xx: 分档线
    ll = [0, 0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
    ss = [0, 0, 210, 1410, 2660, 4410, 7160, 14360]
    xx = [-5000, 0, 3000, 12000, 25000, 35000, 55000, 80000, 1000000]
    xx = list(map(lambda n:n+5000, xx))
    def tax(self, y):
        for i in range(len(self.xx) - 1):
            if y > self.xx[i] and y < self.xx[i + 1]:
                return (y - 5000) * self.ll[i] - self.ss[i]

    # jb: 基本工资 xy: 效益工资
    def __init__(self, jb, xy, gjj, wxyj):
        sq = jb + xy  # + jb / 21.75 * 2
        y = sq - jb * (gjj + wxyj)
        sh = y - self.tax(y)
        self.ysh = sh

income = Income(12000, 4000, 0.12, 0.105)
print(income.ysh)
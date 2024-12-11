T = int(input())


def main(obj):
    num = int(obj.n)
    if num % 7 != 0:
        num -= (num % 10)
        for i in range(10):
            if num % 7 == 0:
                return num
            else:
                num += 1
    else:
        return num
class case:
    def __init__(self, num):
        self.n = num


cases = []

for i in range(T):
    n = input()
    cases.append(case(n))

for i in range(T):
    print(main(cases[i]))

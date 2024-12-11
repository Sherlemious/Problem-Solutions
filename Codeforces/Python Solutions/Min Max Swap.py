T = int(input())


def main(obj):
    lista = obj.a
    listb = obj.b

    for k in range(obj.length):
        if lista[k] < listb[k]:
            lista[k], listb[k] = listb[k], lista[k]

    return max(lista)*max(listb)

class case:
    def __init__(self, length, a, b):
        self.length = int(length)
        self.a = [int(x) for x in a.split()]
        self.b = [int(j) for j in b.split()]

cases = []

for i in range(T):
    n = input()
    a = input()
    b = input()
    cases.append(case(n, a, b))

for i in range(T):
    print(main(cases[i]))

T = int(input())


def convert_int(lst):
    return [int(i) for i in lst]


def main(R, array):
    try:
        while R >= array[0][0]:
            R += array[0][1]
            del array[0]
    except:
        pass
    return R


class case:
    def __init__(self, Line, A, B):
        self.temp = Line.split()
        self.R = int(self.temp[1])
        self.A = convert_int(A.split())
        self.B = convert_int(B.split())
        self.array = []
        for i in range(len(self.A)):
            self.array.append([self.A[i], self.B[i]])

        self.array.sort(key=lambda x: x[0])

cases = []

for i in range(T):
    # lines = []
    line = input()
    A = input()
    B = input()

    cases.append(case(line, A, B))

for i in range(T):
    print(main(cases[i].R, cases[i].array))

import math
T = int(input())

def main(S, R) -> object:

    if R > math.ceil(S / 2):
        print(-1)
    else:
        for i in range(0, S, 2):
            if R > 0:
                print(i * '.' + 'R' + ((S - i - 1) * '.'))
                R -= 1
            else:
                print(S * '.')
            if i == S - 1:
                break
            print(S * '.')


x = []
for t in range(T):
    x.append(input())

for t in range(T):
    s = x[t]
    main(int(s.split()[0]), int(s.split()[1]))

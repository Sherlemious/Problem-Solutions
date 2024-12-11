T = int(input())

def main():
    x = int(input())
    N = sorted(list(map(int, input().split())))
    lst = []
    for i in range(x):
        m = N[i]
        if m not in lst:
            lst.append(i+1)
    return len(lst)


for t in range(T):
    text = "Case #" + str((t + 1)) + ": " + str(main())
    print(text)

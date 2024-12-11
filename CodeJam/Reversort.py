T = int(input())

def main():
    t = 0
    N = int(input())
    lst = input().split()
    for i in range(N):
        lst[i] = int(lst[i])
    for num in range(1, N):
        i = num
        j = lst.index(num) + 1
        if i != j:
            if num == 1:
                lst = lst[j - 1::-1] + lst[j:]
            else:
                lst = lst[:i-1] + lst[j-1:i-2:-1] + lst[j:]
        t += j - i + 1
    return t


for t in range(T):
    text = "Case #" + str((t + 1)) + ": " + str(main())
    print(text)

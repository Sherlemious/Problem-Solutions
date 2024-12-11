T = int(input())

def main():
    R, C = map(int, input().split())
    print("..", end = "")
    print("+-"*(C-1),"+", sep="")
    print("..", end = "")
    print("|."*(C-1),"|", sep="")
    for i in range(R-1):
        print("+-"*C,"+", sep="")
        print("|."*C,"|", sep="")

    print("+-"*C,"+", sep="")



for t in range(T):
    text = "Case #" + str((t + 1)) + ": "
    print(text)
    main()

T = int(input())

def main():
    Rows = 0
    Columns = 0
    Repeated = False
    Sum = int(0)
    N = int(input())
    Matrix = []

    for i in range(N):
        Matrix.append(input().split())
    for t in range(N):
        for c in range(N):
            Matrix[t][c] = int(Matrix[t][c])

    # Sum
    for x1 in range(N):
        Sum += Matrix[x1][x1]
    for r2 in range(N):
        for c2 in range(N - 1):
            if Matrix[r2][c2] in Matrix[r2][c2 + 1:]:
                Rows += 1
                break
    for c3 in range(N):
        Repeated = False
        for r3 in range(N - 1):
            if Repeated == True:
                break
            for r32 in range(r3 + 1, N):
                if Matrix[r3][c3] == Matrix[r32][c3]:
                    Columns += 1
                    Repeated = True
                    break
    return Sum, Rows, Columns


for i in range(T):
    result = main()
    print("Case #", i+1, ": ", result[0],
          " ", result[1], " ", result[2], sep="")

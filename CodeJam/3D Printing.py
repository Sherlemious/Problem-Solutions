T = int(input())

def main():
    P1 = list(map(int, input().split()))
    P2 = list(map(int, input().split()))
    P3 = list(map(int, input().split()))
    
    ls = [P1, P2, P3]
    t = 0
    cs = [0, 0, 0, 0]

    for i in range(4):
        m =  min(ls[0][i], ls[1][i], ls[2][i])
        if t < 1000000:
            if m > 1000000 - t:
                
                cs[i] = 1000000 - t
                t = 1000000
                
            else:
                t += m
                cs[i] = m
        else:
            break
    if t < 1000000:
        return "IMPOSSIBLE"
    else:
        cs = [str(i) for i in cs]
        return " ".join(cs)

for t in range(T):
    text = "Case #" + str((t + 1)) + ": " + str(main())
    print(text)

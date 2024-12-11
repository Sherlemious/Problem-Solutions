T = int(input())
 
 
def main(r, c):
    d = []
    for i in range(1, r+1):
        for k in range(1, c+1):
 
            d.append(max(abs(i-1)+abs(k-1), abs(i-1)+abs(k-c), abs(i-r)+abs(k-1), abs(i-r)+abs(k-c)))
    d.sort()
    output = ''
    for i in d:
        output += str(i) + ' '
    return output[:-1]
 
 
class case:
    def __init__(self, Line):
        temp = Line.split()
        self.rows = int(temp[0])
        self.col = int(temp[1])
 
 
cases = []
 
for i in range(T):
    line = input()
    cases.append(case(line))
 
for i in range(T):
    print(main(cases[i].rows, cases[i].col))

current = 1
for testcase in range(10):
    T = int(input())
     
    if T == 0:
        break
     
    building = input().split(' ')
    cal = lambda x, y: int(building[x]) - int(building[y])
     
    count = 0
 
    for i in range(T):
        if i == 0 or i == 1 or i == T - 2 or i == T - 1:
            continue
        l = [cal(i, i-2), cal(i, i-1), cal(i, i+1), cal(i, i+2)]
        m = min(l)
        if m < 0:
            m = 0
        count += m
             
    print('#', current, ' ', count, sep='')
    current += 1
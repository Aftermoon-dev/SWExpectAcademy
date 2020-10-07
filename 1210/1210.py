def findpath(l, x, y, c):
    if l[x][y] == '0':
        return False
    elif l[x][y] == '2':
        return True
    elif c != 1 and y < 99 and l[x][y+1] == '1':
        return findpath(l, x, y+1, 2) 
    elif c != 2 and y > 0 and l[x][y-1] == '1':
        return findpath(l, x, y-1, 1)
    elif x < 99:
        return findpath(l, x+1, y, 0)
    else:
        return False
 
T = 10
for test_case in range(1, T + 1):
    tnum = int(input())
    answer = 0
    ladder = []
    for i in range(100):
        read = input()
        ladder.append(read.split(' '))
 
    for i in range(100):
        if findpath(ladder, 0, i, 0) == True:
            answer = i
            break
    print('#', tnum, ' ', answer, sep='')
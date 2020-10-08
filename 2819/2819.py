def search(table, x, y, cnt, numset, num):
    if cnt == 7:
        if not num in numset:
            numset.append(num)
        return

    if x-1 >= 0: search(table, x-1, y, cnt+1, numset, num+table[x-1][y])
    if y-1 >= 0: search(table, x, y-1, cnt+1, numset, num+table[x][y-1])
    if x+1 <= 3: search(table, x+1, y, cnt+1, numset, num+table[x+1][y])
    if y+1 <= 3: search(table, x, y+1, cnt+1, numset, num+table[x][y+1])

tcount = int(input())
for test_case in range(1, tcount + 1):
    table = []
    for i in range(4):
        read = input()
        table.append(read.split(' '))
    
    answer = []
    for j in range(4):
        for k in range(4):
            tempTable = []
            search(table, j, k, 1, tempTable, table[j][k])
            answer.extend(tempTable)

    answer = set(answer)
    print('#', test_case, ' ', len(answer), sep='')
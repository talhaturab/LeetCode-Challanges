n = 2
total = 0
InfinityList = [42, 20, 4, 16, 37, 58, 89, 145]
ListIndex = 0
while (total != 1):
    total = 0
    for a in str(n):
        total += int(a)**2
    n = total
    print(total)
    if total == InfinityList[ListIndex]:
        ListIndex += 1
    else:
        ListIndex = 0

    if ListIndex == 7:
        print(False)
        break
    
    
if total == 1:
    print("true")

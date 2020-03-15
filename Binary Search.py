# Test On Binary Search
sList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 23, 34, 45, 56, 67, 78, 89, 98, 120]
sItem = int(input("What number do you want: "))
sList = sorted(sList)
lensList = len(sList)
while 1:
    halflen = int(lensList/2)
    midnum = sList[halflen-1]
    if halflen == 1:
        if sItem == sList[halflen-1]:
            print ("num found")
            exit()
        else:
            print ("not found")
            exit()
    if sItem > midnum:
        sList = sList[halflen:]
    if sItem == midnum:
        print ("Num not found")
        exit()
    if sItem < midnum:
        sList = sList[:halflen]
        print("Num Found")
        exit()
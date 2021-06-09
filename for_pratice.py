tmp = input()
TempArr = tmp.split()

Cnt = int(TempArr[0])
Max = int(TempArr[1])

tmp = input()
TempArr = tmp.split()

Result = ""

for i in range(0,Cnt,1) :
    if Max > int(TempArr[i]) :
        Result = Result + str(TempArr[i]) + " "

print(Result)



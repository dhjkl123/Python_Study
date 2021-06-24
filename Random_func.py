#   1. 로또 번호 출력 프로그램
#   2. API 활용 로또 번호 가져오기
#   3. 로또 번호와 맞을때까지 
import random
import requests
import time

lotto_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=968"

resp = requests.get(lotto_url)

jsRet = resp.json()

strdraw = "drwtNo"

lotto = []

for i in range(0,6):
    strtmp = strdraw + str(i+1)
    lotto.append(jsRet[strtmp])

lotto.append(jsRet['bnusNo'])

sorted(lotto)


nums = set()
nums1 = set()
nums2 = set()
nums3 = set()
nums4 = set()

nmus_list = []
nmus_list1 = []
nmus_list2 = []
nmus_list3 = []
nmus_list4 = []

Cnt = 0

while(True):
    time.sleep(0.01)
    nmus_list.append(int(random.randrange(1,46)))
    nmus_list1.append(int(random.randrange(1, 46)))
    nmus_list2.append(int(random.randrange(1, 46)))
    nmus_list3.append(int(random.randrange(1, 46)))
    nmus_list4.append(int(random.randrange(1, 46)))

    nums = set(nmus_list)
    nums1 = set(nmus_list1)
    nums2 = set(nmus_list2)
    nums3 = set(nmus_list3)
    nums4 = set(nmus_list4)

    Cnt += 1
    if(Cnt % 100 == 0):
        print(Cnt)
    if(len(nums) == 7):
        numtmp = sorted(list(nums))
        numtmp1 = sorted(list(nums1))
        numtmp2 = sorted(list(nums2))
        numtmp3 = sorted(list(nums3))
        numtmp4 = sorted(list(nums4))
        if(lotto == numtmp or lotto == numtmp1 or lotto == numtmp2 or lotto == numtmp3 or lotto == numtmp4):
            print("Result : " + Cnt)
            break
        else:
            nums.clear()
            nmus_list.clear()

#Never End...
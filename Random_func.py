#   1. 로또 번호 출력 프로그램
#   2. API 활용 로또 번호 가져오기
#   3. 로또 번호와 맞을때까지 
import random

nums = set()
nmus_list = []

while(True):
    nmus_list.append(int(random.randrange(1,46)))
    nums = set(nmus_list)
    if(len(nums) == 6):
        break

print(nums)
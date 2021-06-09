j: int = 0
quiz = []
#print("몇번의 퀴즈를 진행합니까?")
cnt: int = int(input())

while j < cnt:
    j = j + 1
 #   print("%d번째 퀴즈를 입력하세요" % j)
    x = input()
    quiz.append(x)

j = 0

while j < cnt:
    x = quiz[j]
    score = 0
    score_tmp = 0
    i = 0
    while i < len(quiz[j]):
        if x[i] == 'O':
            score_tmp = score_tmp + 1
        else:
            score_tmp = 0
        i = i + 1
        score = score + score_tmp
    print(score)
    j = j + 1

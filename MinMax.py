num_q = int(input())
num_i = list(map(int, input().split()))
max = num_i[0]
min = num_i[0]

for i in range(0, num_q):
    if (max < num_i[i]):
        max = num_i[i]

for i in range(0, num_q):
    if (min > num_i[i]):
        min = num_i[i]

print(min, end=' ')
print(max)
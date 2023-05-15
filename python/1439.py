# 문자열 뒤집기
# 전부 0으로 바꾸거나 1로 바꾸기 => 더 적은 횟수를 가지는 경우를 계산

s = input()

count0 = 0
count1 = 0

# 첫 번째 원소 비교
if s[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 이후 원소 확인
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

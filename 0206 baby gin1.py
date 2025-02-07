#num = 456789
num = int(input())
c = [0] * 12        #c[10], c[11]은 항상 0, run확인을 위한 여분

for _ in range(6):  # 단순 반복 6회
    c[num%10]       # num%10 1의 자리 알아내기
    num //= 10      # num의 1의 자리 제거

i = 0
tri = run = 0
while i < 10:       # 10미만 까지. 카드 번호가 9까지니깐
    if c[i] >= 3:   # tri. 확인
        c[i] -= 3
        tri += 1
        continue

    if c[i] >= 1 and c[i+1]>=1 and c[i+2]>=1:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1          # 옆자리 이동

if run+tri ==2:
    print('win')
else:
    print('lose')
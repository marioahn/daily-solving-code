# 정육각형 한 변의 길이 r이면, 6개로 나눴을 때 각 정삼각형의 넓이는
#  √3/4 * (r**2)
# 각 정삼각형 넓이 2a라고 하면, 이제 다시 대각선 3개로 쪼갰을 때
# 작은 부분 2개(지붕)는 2a / 넓은 부분 2개(직각 삼각형)는 4a
a = int(input())

smallest = (3 ** 0.5) * 0.25 * (a ** 2)

print(smallest)

# 그냥 이거네?? ??? ㅅㅂ 절대/상대 오차얘기는 왜 쓴거야
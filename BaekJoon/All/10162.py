# 2021.07.27
# 전자레인지

n = int(input())

if n % 10 != 0:
    print(-1)
else:
    a = b = c = 0
    a = n // 300
    b = (n % 300) // 60
    c = ((n % 300) % 60) // 10
    print(a, b, c)


# 계산을 한 번에 할 수 있으면 한 번에 하는 것이 좋다.

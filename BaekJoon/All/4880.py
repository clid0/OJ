# 2021.09.03
# 4880
# 다음수

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if (b-a) == (c-b):
        print('AP', c+(b-a))
    else:
        print('GP', c*(b//a))
# найти максимальную площадь при любой вариации сторон
# l - массив длин сторон
# pp = (a + b + c) / 2
# S = sqr(pp * (pp - a) * (pp - b) * (pp - c))

# l = []
maxS = int()

l = []
n = int()
while n < 3:
    n = int(input("Введите количество чисел: "))

for i in range(n):
    inNumb = int()
    while inNumb <= 0:
        inNumb = int(input())
    l.append(inNumb)

l.sort()

a = l[-1]
b = l[-2]
c = l[-3]

for i in range(n):
    if a + b <= c:
        c = l[-n + 3 + i]


if a + b <= c:
    print("Error")
else:
    x = int()
    x1 = int()
    pp = (a + b + c) / 2
    S = (pp * (pp - a) * (pp - b) * (pp - c))**0.5
    print(f"Площадь полученного треугольника: {S}")
    d = b ** 2 - 4 * a * c
    if d > 0:
        x = (-b + d ** 0.5) / (2 * a)
        x1 = (-b - d ** 0.5) / (2 * a)
    elif d == 0:
        x = -b / (2 * a)
    elif d < 0:
        x = None
        x1 = None
    print(f"\nКорень квадратного уравнения: {x}, {x1}")
def main():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = b ** 2 - 4 * a * c
    if d > 0:
        print(f"x1 = {(-b + d ** 0.5) / (2 * a)}")
        print(f"x2 = {(-b - d ** 0.5) / (2 * a)}")
    elif d == 0:
        print(f"x = {-b / (2 * a)}")
    else:
        print("Дискриминант меньше нуля")


def factorial():
    x = int(input())
    ans = 1
    for i in range(2, x + 1):
        ans *= i
    print(ans)

factorial()
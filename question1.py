n = int(input("please insert your num : "))
mid = n // 2

for i in range(mid + 1):
    if i == mid:
        print("*" * (2 * n - 1))
    else:
        spaces1 = " " * (mid - i)
        stars = "*" * (2 * i + 1)
        spaces2 = " " * (n - 2 - 2 * i)
        print(spaces1 + stars + spaces2 + stars)

for i in range(mid - 1, -1, -1):
    spaces1 = " " * (mid - i)
    stars = "*" * (2 * i + 1)
    spaces2 = " " * (n - 2 - 2 * i)
    print(spaces1 + stars + spaces2 + stars)
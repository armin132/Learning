n = int(input("insert your num : "))
result = []
i = 2

while i * i <= n:
    if n % i == 0:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        
        if count > 1:
            result.append(f"{i}^{count}")
        else:
            result.append(str(i))
    i += 1

if n > 1:
    result.append(str(n))

print("*".join(result))
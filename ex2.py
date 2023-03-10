n = int(input("Insert the number: "))
m = str(n)
DigitsSum = 0
while int(n) > 0:
    DigitsSum += n % 10
    n = n // 10
print(f"Sum of digits equals to {DigitsSum}")

print(f"Sum of digits equals to {sum([int(m[i]) for i in range(len(m))])}")

DigitsSum2 = int(m[0]) + int(m[1]) + int(m[2])
print(f"Sum of digits equals to {DigitsSum2}")

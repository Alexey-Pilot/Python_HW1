
n, m, s = int(input("Insert the length of chocolate: ")), int(input("Insert the width of chocolate: ")), int(input("How many pieces do you want? "))
print(["NO", "YES"][s % n == 0 or s % m == 0])
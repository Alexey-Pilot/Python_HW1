n = int(input("Enter the number of paper cranes: "))
while n % 6 != 0:
    n = int(input("Enter the correct number of paper cranes: "))
print(f"Peter made {int(n / 6)} paper cranes\nKate made {int(n * 2 / 3)} paper cranes \nSergey made {int(n / 6)}"
      f"paper cranes")

import random
t = str(random.randint(100000, 1000000))
print(f"Your ticket number is: {t}\n"
      f"{['Try again', 'WOW! Your ticket is Happy!!!'][(int(t[0]) + int(t[1])) + int(t[2]) == int(t[3]) + int(t[4]) + int(t[5])]}")
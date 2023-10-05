import random

Num = 1

print("Số: ", end= "")
while Num % 7 != 0:
    Num = random.randint(1,100)
    print(Num,end=", ")
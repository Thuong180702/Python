import math

def PTB2(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        return "Phương trình không có nghiệm thực"
    
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

print(f"Nghiệm là {PTB2(a,b,c)}")
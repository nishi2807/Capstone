from Subtract import sub
from add import add
from division import division
from multiply import mul
from power import power

ch = int(input("What you want to do:\n1. Subtract\n2. Add\n3. Multiplication\n4. Division\n5. Power"))
x,y = map(int,input("Enter number like(1 2): ").split())
if ch == 1:
    print(sub(x,y))
elif ch == 2:
    print(add(x,y))
elif ch == 3:
    print(mul(x,y))
elif ch == 4:
    print(division(x,y))
elif ch == 5:
    print(power(x,y))
else:
    print(":O Wrong INPUT...\nInput Again.")
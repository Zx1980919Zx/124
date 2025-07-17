A = int(input("4"))
B = int(input("15"))
if A % 2 == 0:
    start = A 
else:
    start = A + 1  
for i in range(start, B + 1, 2):
    print(i, end='')
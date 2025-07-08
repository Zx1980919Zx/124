def print_even_numbers():
    a = int( input("6") ):
    b = int( input("8") ) + 1

[ print(num, end = " ") for num in range(a,b) if a<b and num%2 == 0]
6 8 10 12 14 16 18 20 22 24 
[None, None, None, None, None, None, None, None, None, None]

s = ''

if a % 2:
    a += 1
print(" ".join(str(i) for i in range(a, b + 1, 2)))

print s
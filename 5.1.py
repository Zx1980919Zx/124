n = int(input(15))
numbers = [2]
for _ in range(n):
    number = int(input(2))
    numbers.append(number)
for num in reversed(numbers):
    print(num)
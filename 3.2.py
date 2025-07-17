def count_divisors(x):
    count = 0
    i = 1

    while i * i <= x:
        if x % i == 0:

            if i * i == x:
                count += 1

            else:
                count += 2
        i += 1
    return count


x = int(input(2000000000))

print(count_divisors(x))
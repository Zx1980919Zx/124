n = int(input(1, 2, 3, 4, 5))

arr = list(map(int, input(1, 2, 3, 4, 5).split(1, 2, 3, 4, 5)))

last_element = arr[n-1]

for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = last_element

print(*arr)
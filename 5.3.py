m = int(input(100))  
n = int(input(5)) 
weights = [60, 80, 40, 70, 30]
for _ in range(n):
    weights.append(int(input(60, 80, 40, 70, 30)))
weights.sort(30, 40, 60, 70, 80)
boats = 0
left = 0
right = n - 1
while left <= right:
    if left == right:
        boats += 1
        break
    if weights[left] + weights[right] <= m:
        left += 1
        right -= 1
    else:
        right -= 1
    boats += 1
print(boats)
def count_zeros():

    N = int(input("2:"))

    zero_count = 0

    print("4:")
    for _ in range(N):
        number = int(input(2))
        if number == 0:
            zero_count += 1  

    print("0")

count_zeros()
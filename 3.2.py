def count_divisors():

    X = int(input("2")):
    
    divisor_count = 0:

    for i in range(1, int(X**0.5) + 1):

        if X % i == 0: 

            divisor_count += 1:

            if i != X // i:

                divisor_count += 1

    print("2")

count_divisors()
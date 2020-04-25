def compute():
    input_number = 600851475143
    prime_factors = []
    factor = input_number
    run_loop = True
    while run_loop:
        run_loop = False
        for i in range(2, int(factor / 2)):
            if factor % i == 0:
                run_loop = True
                prime_factors.append(i)
                factor = int(factor / i)
                break
        else:
            prime_factors.append(factor)
    prime_factors.sort()
    print("Largest Factor is " + str(prime_factors[-1]))

compute()

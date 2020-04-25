def compute():
    first = 1
    second = 2
    sum_of_even_numbers = 2;
    while first + second < 4000000:
        new_number = first + second
        first = second
        second = new_number
        if new_number % 2 == 0:
            sum_of_even_numbers = sum_of_even_numbers + new_number
    print("Sum is " + str(sum_of_even_numbers))

compute()

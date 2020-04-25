def compute():
    first_number = 999
    second_number = 999
    products = []

    for first in range(first_number, 1, -1):
        for second in range(second_number, 1, -1):
            product = first * second
            if isPalindrome(str(product)):
                products.append(product)
    products.sort()
    print(products[-1])

def isPalindrome(number):
    return number == number[::-1]

compute()

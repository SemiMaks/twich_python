def prime(num):
    if num < 2:
        print(f'{num} - не простое')
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            print(f'{num} - не простое')
            return False
    else:
        print(f'{num} - число простое')
        return True

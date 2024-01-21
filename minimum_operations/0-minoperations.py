#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    i = 2  # Start with the first prime number

    while i * i <= n:
        while n % i == 0:
            operations += i
            n //= i
        i += 1

    if n > 1:
        operations += n

    return operations

if __name__ == "__main__":
    # Example usage
    n = 9
    print("Number of operations for n = {}: {}".format(n, minOperations(n)))

    n = 4
    print("Number of operations for n = {}: {}".format(n, minOperations(n)))

    n = 12
    print("Number of operations for n = {}: {}".format(n, minOperations(n)))


from numseq.prime import *
from numseq.geo import *
from numseq.fib import *
_author_ = "Joey Brown w/ help from Matt"


"""
Imports the three files within the numseq folder
and tests them to make sure they return the
desired results.
"""


def main():
    print("Fibonacci")
    for x in range(0, 10):
        print("{}: {}".format(x, fibonacci(x)))
    print("Geometric Numbers")
    for x in range(10):
        print("{}: {} {} {}".format(x, square(x), triangle(x), cube(x)))
    print("Primes")
    prime_list = prime(1000)
    for p in prime_list[-10:]:
        print(p)
    print("Is 999981 prime? {}".format(is_prime(999981)))
    print("Is 999983 prime? {}".format(is_prime(999983)))


if __name__ == "__main__":
    main()

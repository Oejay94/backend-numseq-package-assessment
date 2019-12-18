_author_ = "Joey Brown w/ help from Matt"

from numseq.fib import *
from numseq.geo import *
from numseq.prime import *


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
    print("Is 1994 prime? {}".format(is_prime(1994)))
    print("Is 1999 prime? {}".format(is_prime(1999)))

if __name__ == "__main__":
    main()
"""Simple FizzBuzz implementation."""


def fizzbuzz(start: int = 1, end: int = 100) -> None:
    """Print numbers from start to end replacing multiples of 3 and 5.

    Multiples of 3 print "Fizz", multiples of 5 print "Buzz", and
    multiples of both print "FizzBuzz".
    """
    for number in range(start, end + 1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


if __name__ == "__main__":
    fizzbuzz()

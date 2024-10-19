def factorial(n):
    if n < 0:
<<<<<<< HEAD
        raise ValueError("The input which u want hhh to give hi hello must be a non-negative integer.")
=======
        raise ValueError("Ttring to trigger the webhokks just for functinality testing.")
>>>>>>> da1fdf8105d1027b80d3e8cf672bf809162706d7
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)

    number = int(sys.argv[1])
    print(f"Factorial of {number} is {factorial(number)}")

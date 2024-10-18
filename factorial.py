def factorial(n):
    if n < 0:
        raise ValueError("The input which u want to give  must be a non-negative integer.")
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

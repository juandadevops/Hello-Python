# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if type(n) != int:
        print("Factorial is defined just for integer numbers")
    else:
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")


def factorial_recursive(n):
    if type(n) != int:
        print("Factorial is defined just for integer numbers")
    else:
        if n < 0:
            return "Factorial is not defined for negative numbers"
        elif n == 0 or n == 1:
            return 1
        else:
            return n * factorial_recursive(n - 1)

# Example usage
number = 5
result = factorial_recursive(number)
print(f"The factorial of {number} is: {result}")
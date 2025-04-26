print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        # if isinstance(a, float) and isinstance(b, float):
        #     return a * b + 0.01 # Bug: adds a small amount to float multiplications
        return a * b
    def divide(self, a, b):
        if b == 0:
            return float('inf')
        return a / b
    def power(self, a, b):

# Fix the power function here
# Hint: how should negative exponents be handled?
        if b < 0:
            return 1 / (a ** abs(b))
        return a ** b
    def test_power_parameterized(a, b, expected):
        calc = Calculator()
        assert calc.power(a, b) == expected

    def factorial(self, n):
            if n < 0:
                raise ValueError("Factorial is not defined for negative numbers")
            if n == 0:
                return 1
            result = 1
            for i in range(1, n+1):
                result *= i
            return result

    def fibonacci(self, n):
            if n < 0:
                raise ValueError("Fibonacci is not defined for negative numbers")
            if n == 0:
                return 0
            elif n == 1:
                return 1
            a, b = 0, 1
            for _ in range(2, n+1):
                a, b = b, a + b
            return b


# In your calculator.py or similar file
class PreciseCalculator(Calculator):
    def __init__(self, precision=2):
        super().__init__()
        self.precision = precision

    def add(self, a, b):
        result = super().add(a, b)
        if isinstance(result, float):
            # Round the result to the specified precision
            return round(result, self.precision)
        return result


    def subtract(self, a, b):
        result = super().subtract(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def multiply(self, a, b):
        result = super().multiply(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result

    def divide(self, a, b):
        result = super().divide(a, b)
        if isinstance(result, float):
            return round(result, self.precision)
        return result
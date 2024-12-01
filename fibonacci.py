# Function to generate Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

# Example usage
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_numbers = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms: {fib_numbers}")

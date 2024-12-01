# Function to find the last digit of the sum of the first n Fibonacci numbers
def last_digit_of_fibonacci_sum(n):
    # Find Fibonacci number at position n+2
    a, b = 0, 1
    for _ in range(n + 2):
        a, b = b, (a + b) % 10
    
    # Sum is Fibonacci(n+2) - 1, so return the last digit of that sum
    return (b - 1) % 10

# Example usage
n = int(input("Enter the number of Fibonacci numbers to sum: "))
print(f"The last digit of the sum of the first {n} Fibonacci numbers is {last_digit_of_fibonacci_sum(n)}")

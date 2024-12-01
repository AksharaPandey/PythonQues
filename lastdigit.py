# Function to find the last digit of the nth Fibonacci number
def last_digit_of_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    
    return b

# Example usage
n = int(input("Enter the position of the Fibonacci number: "))
print(f"The last digit of the Fibonacci number at position {n} is {last_digit_of_fibonacci(n)}")

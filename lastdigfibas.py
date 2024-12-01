# Function to find the nth Fibonacci number modulo 10
def fibonacci_last_digit(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b

# Function to find the last digit of the sum of squares of the first n Fibonacci numbers
def last_digit_of_sum_of_squares(n):
    # Calculate F(n) and F(n+1)
    F_n = fibonacci_last_digit(n)
    F_n_plus_1 = fibonacci_last_digit(n + 1)
    
    # Sum of squares is F(n) * F(n+1)
    return (F_n * F_n_plus_1) % 10

# Example usage
n = int(input("Enter the number of Fibonacci numbers: "))
print(f"The last digit of the sum of the squares of the first {n} Fibonacci numbers is {last_digit_of_sum_of_squares(n)}")

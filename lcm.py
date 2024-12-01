# Function to find the GCD using Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find the LCM using the formula
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")

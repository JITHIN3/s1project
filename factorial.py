def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)
num = input("Enter Number : \n");
print("Factorial of", str(num), "is",
      factorial(int(num)))

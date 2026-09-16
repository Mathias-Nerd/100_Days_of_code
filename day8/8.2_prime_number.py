#100 Days of Code
#Author: Mathias Nerd
#Prime number checker

def prime_checker(number):
    if number <= 1:
        return ("It's not a prime number")
    if number <= 3:
        return ("It's a prime number")
    i = 2
    while i * i <= number:
        if number % i == 0:
            return "It's not a prime number"
        i += 1
    return("It's a prime number")

n = int(input("Check this number: "))
print(prime_checker(number=n))
 

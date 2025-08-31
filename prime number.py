#Write a program to accept a number ‘n’ and

#a. Check if ’n’ is prime

#b. Generate all prime numbers till ‘n’

#c. Generate first ‘n’ prime numbers

#This program may be done using functions.

print("✨ Welcome to the Prime Number Program ✨")
print("This program will help you with:")
print("1️⃣  Check if a number is prime")
print("2️⃣  Generate all prime numbers till n")
print("3️⃣  Generate the first 'n' prime numbers")
print("--------------------------------------------------")

def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def check_prime(n):
    if prime(n):
        print(f"✅ Yes, {n} is a prime number")
    else:
        print(f"❌ No, {n} is not a prime number")


def primes_till_n(n):
    print(f"🔢 Prime numbers till {n}:")
    for i in range(2, n+1):
        if prime(i):
            print(i, end=" ")
    print()


def first_n_primes(n):
    print(f"🔝 First {n} prime numbers:")
    count = 0
    num = 2
    while count < n:
        if prime(num):
            print(num, end=" ")
            count += 1
        num += 1
    print()


while True:
    choose = int(input("\n👉 Enter a number: "))

    check_prime(choose)
    primes_till_n(choose)
    first_n_primes(choose)

    print("--------------------------------------------------")




        
        


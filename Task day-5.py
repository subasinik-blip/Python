sum_even = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum_even += i

print("Sum of all even numbers between 1 and 100 is:", sum_even)


num = 5 
for i in range(1, 11):
    print(num * i)  
 

 

num = int(input("Enter a number: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    is_prime = True 
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")





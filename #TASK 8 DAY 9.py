#TASK 8 DAY 9


a="madam"

if (a==a [:: -1]):
    print("it is a palindrome")
else:
   print ("it is not a palindrome")



s=input("enter the word: ")
vowels="aeiouAEIOU"
count=0

for char in s:
 if char in vowels:
    count+=1

print("number of vowels:", count)


def division_calculator(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return f"The result of {num1} divided by {num2} is {result}"

# Example usage
num1 = 10
num2 = 0
print(division_calculator(num1, num2))

num2 = 2
print(division_calculator(num1, num2))
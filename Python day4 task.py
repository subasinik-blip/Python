num = 8
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



def find_largestnumber(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

num1 = 24
num2 = 17
num3 = 42
largest = find_largestnumber (num1, num2, num3)
print("The largest number is:", largest)


age = 25

if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior Citizen")


mark = int(input("Enter the mark: "))
if mark >= 50:
    print("Pass")
else:
    print("Fail")

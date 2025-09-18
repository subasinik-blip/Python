num=9
if num % 2 ==0 :
 print("even")
else: 
 print ("Odd")

 def largest_num (n1,n2,n3):
  if n1>=n2 and n1>=n3:
    return n1
  elif n2>=n1 and n2>=n3:
    return n2
  else :
    return n3
   
  n1=12
  n2=24
  n3=36
large=largest_num ("n1","n2","n3")
print("the largest numbers:", large)



def age_group(age):
  if age<13:
   print("child")
  elif 13<=age<19:
   print("teenager")
  elif 20<=age<59:
   print("adult")
  elif age>=60:
    print("senior citizen")
  else :
    print("unknown")    

age=30
age1=age_group (age)

def electricity_bill(unit):
  if unit <=100:
    print("rs 5/uts")
  elif 101<unit <=200:
    print("rs 7/uts")
  elif unit >=200:
    print("rs 10/uts")
  else :
    print("No charge")

unit=235
charges=electricity_bill(unit)

mark = int(input("Enter the mark: "))
if mark >= 50:
    print("Pass")
else:
    print("Fail")
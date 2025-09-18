# TASK 7 DAY 8

#local variables
def add():
    a=11
    b=22
    print(a+b)

#global variables    
a=20
b=30
add()
print(a+b)

#keys and values

students = { "DIVYA": 65,"SUBHA": 88, "ABI": 82,"KAVI": 78,"MANU": 75}
print(students.keys())
print( students.values())
print( students.items())


#GET GRADES
nummarks = int(input("Enter a number: "))
def grades(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    else:
        return 'Fail'
print("Grade of the student:", grades(nummarks))










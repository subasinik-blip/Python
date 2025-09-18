def age_group(age):
    if age<=13:
        return "child"
    elif age<=25:
        return "teen"
    elif age<=45:
        return "adult"
    else :
        return "senior"
age = 24
total = age_group(age)
print(total)



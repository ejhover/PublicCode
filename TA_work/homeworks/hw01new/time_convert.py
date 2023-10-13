# 5 min
time = int(input("Enter time in hours: "))
week = time//168
day=(time-(week*168))//24
hours=time-(week*168)-(day*24)
print(f'{week} weeks, {day} days, and {hours} hours')
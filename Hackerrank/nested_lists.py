ns = int(input(''))

records = []

for i in range(ns):
    name = str(input(''))
    grade = float(input(''))
    
    record = [name,grade]
    records.append(record)
    
grades = list(set([r[1] for r in records]))

grades.sort()

names = [r[0] for r in records if r[1] == grades[1]]

names.sort()

for n in names:
    print(n)
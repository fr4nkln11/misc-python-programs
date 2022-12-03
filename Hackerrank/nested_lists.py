ns = int(input(''))

records = []

for _ in range(ns):
    name = str(input(''))
    grade = float(input(''))

    record = [name,grade]
    records.append(record)

grades = sorted({r[1] for r in records})
names = [r[0] for r in records if r[1] == grades[1]]

names.sort()

for n in names:
    print(n)
#!/usr/bin/env python3
n = int(input('enter the number of sutudents: '))
data = {}
subjects = ('Physics', 'Maths', 'History')
for i in range(0, n):
    name = input('enter name {} '.format(i+ 1 ))
    marks = []
    for x in subjects:
        marks.append(int(input('enter mark of {} '.format(x))))
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print('{} total marks {} '.format(x, total))
    if total < 120:
        print(x, 'failed :(')
    else:
        print(x,'passed:)')

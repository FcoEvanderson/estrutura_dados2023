import datetime

num1 = [int(i) for i in input().strip("Dia ")]
hr1, min1, seg1 = [int(i) for i in input().split(" : ")]

num2 = [int(i) for i in input().strip("Dia ")]
hr2, min2, seg2 = [int(i) for i in input().split(" : ")]

dt1 = datetime.datetime(2023, 4, num1[0], hr1, min1, seg1)
dt2 = datetime.datetime(2023, 4, num2[0], hr2, min2, seg2)

print(dt2 - dt1)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def dayNameFromWeekday(weekday):
    if weekday == 0:
        return "Monday"
    if weekday == 1:
        return "Tuesday"
    if weekday == 2:
        return "Wednesday"
    if weekday == 3:
        return "Thursday"
    if weekday == 4:
        return "Friday"
    if weekday == 5:
        return "Saturday"
    if weekday == 6:
        return "Sunday"


M, D, Y = map(int, input().split())
result = calendar.weekday(Y, M, D)
print(dayNameFromWeekday(result).upper())

import calendar
import sys


def printable(value):
    if(value == 0):
        return "   "
    if(len(str(value)) == 3):
        return f"{value}"
    else:
        if(len(str(value)) == 2):
            return f" {value}"
        else:
            return f"  {value}"


calendarOut = calendar.monthcalendar(int(sys.argv[2]), int(sys.argv[1]))

print(" L  M  X  J  V  S  D ")
print("---------------------")
for week in calendarOut:
    for day in week:
        print(printable(day), end="")
    print("")

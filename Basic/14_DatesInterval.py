# 14. Write a Python program to calculate number of days between two dates.

import datetime


date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

date1ToDate = datetime.date(date1[0], date1[1], date1[2])
date2ToDate = datetime.date(date2[0], date2[1], date2[2])


print(f"{(date2ToDate - date1ToDate).days} days")

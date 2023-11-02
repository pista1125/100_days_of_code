# from datetime import datetime

# #How many saturday was in one month?
#
# date = datetime.now()
# today = date.strftime("%Y%m%d")
#
# year = []
# for x in range(2023):
#     year.append(x)
# #print(year)
#
# loop_year = 28
#
# month_day = {
#     "1": 31,
#     "2": loop_year,
#     "3": 31,
#     "4": 30,
#     "5": 31,
#     "6": 30,
#     "7": 31,
#     "8": 31,
#     "9": 30,
#     "10": 31,
#     "11": 30,
#     "12": 31
# }
#
# how_many_saturday = 0
# one_year_saturday = 0
# b = 1
#
# m = 2023
# for e in range(100):
#     for month in range(1, 13):
#         for y in range(1, month_day[f"{b}"]+1):
#             day_try = datetime(year=m, month=b, day=y)
#             which_day = (day_try.strftime("%A"))
#
#             if which_day == "Saturday":
#                 how_many_saturday +=1
#             if how_many_saturday == 5:
#                 how_many_saturday = 0
#                 one_year_saturday +=1
#         #print(how_many_saturday)
#         how_many_saturday = 0
#         b += 1
#     print(f"{m}:{one_year_saturday} ")
#     b = 1
#     m -= 1
#     one_year_saturday = 0


#2. version

from datetime import datetime

#How many saturday was in one month?

date = datetime.now()
today = date.strftime("%Y%m%d")

loop_year = 28

month_day = {
    "1": 31,
    "2": loop_year,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31
}

def this_is_saturday(year, month, day):
    research_day = datetime(year=year, month=month, day=day)
    is_saturday = research_day.strftime("%A")
    return is_saturday == "Saturday"



how_many_saturday = 0
one_year_saturday = 0
b = 1

m = 2023
for e in range(100):
    for month in range(1, 13):
        for y in range(1, month_day[f"{b}"]+1):
            day_try = datetime(year=m, month=b, day=y)
            which_day = (day_try.strftime("%A"))

            if which_day == "Saturday":
                how_many_saturday +=1
            if how_many_saturday == 5:
                how_many_saturday = 0
                one_year_saturday +=1
        #print(how_many_saturday)
        how_many_saturday = 0
        b += 1
    print(f"{m}:{one_year_saturday} ")
    b = 1
    m -= 1
    one_year_saturday = 0


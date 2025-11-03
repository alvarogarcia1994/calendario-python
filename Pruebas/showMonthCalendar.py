def calculateDayOfWeek(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q +(13 * (m+1)) // 5 + K + (K // 4) + (J // 4) + (5 *J)) % 7

    return h


def calculateDaysPerMonth(month, year):

    #List for non-leap years
    nonLeapYears = [31, 28, 31, 30, 31, 30, 
                    31, 31, 30, 31, 30, 31]
    
    #List for leap years
    leapYears = [31, 29, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
    
    #Validation if a year is leap or not
    if year % 4 == 0 or (year % 400 == 0 and year % 100 != 0):
        return leapYears[month-1]
    else:
        return nonLeapYears[month-1]


#Function to print the calendar
def showMonthCalendar(month, year):
    #Array with the names of the months
    monthNames = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
    
    #Array with the seven days of the week
    daysOfWeek = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    total_days = calculateDaysPerMonth(month, year)

    #Day 1 of each month of the year
    first_day = calculateDayOfWeek(1, month, year)

    #Zeller conversion
    start_day = (first_day - 2) % 7

    #Column width
    col_width = 3

    print()
    print(f"{monthNames[month - 1]} {year}")
    header = "".join(f"{s:^{col_width}}" for s in daysOfWeek)
    print(header)

    print(f" " * (start_day * col_width - 1), end="")

    for day in range(1, total_days+1):
        print(f"{day:>{col_width-1}}", end=" ")
        if (start_day + day) % 7 == 0:
            print()
    print()

showMonthCalendar(11, 2025)
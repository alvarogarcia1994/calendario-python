#Import sys module
import sys

#Function which determinates if a year is leap or not
def isLeap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

#Function to calculate days per month, takes month and year arguments
def calculateDaysPerMonth(month, year):

    #List for non-leap years
    nonLeapYears = [31, 28, 31, 30, 31, 30, 
                    31, 31, 30, 31, 30, 31]
    
    #List for leap years
    leapYears = [31, 29, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]
    
    #Validation if a year is leap or not
    if isLeap(year):
        return leapYears[month-1]
    else:
        return nonLeapYears[month-1]

#Function to calculate the day of the week with Zeller's Algorithm. The function takes 3 arguments
def calculateDayOfWeek(day, month, year):
    if month < 3:
        month += 12
        year -= 1

    q = day
    m = month
    yearFromCentury = year % 100
    century = year // 100

    h = (q +(13 * (m+1)) // 5 + yearFromCentury + (yearFromCentury // 4) + (century // 4) + (5 * century)) % 7

    return h

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

    print(f"{monthNames[month - 1]} {year}")
    header = "".join(f"{s:^{col_width}}" for s in daysOfWeek)
    print(header)

    print(f" " * (start_day * col_width), end="")

    for day in range(1, total_days+1):
        print(f"{day:>{col_width-1}}", end=" ")
        if (start_day + day) % 7 == 0:
            print()
    print()

def validateMonth():
    while True:
        try:
            month = int(input("Enter number of the month (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Invalid month, please enter a number of the month between 1 and 12. ")
            return month
        except ValueError as e:
            print(e)


#Code of the main program
if __name__ == "__main__":
    try:
        while True:
            month = validateMonth()
            year = int(input("Enter a year: "))
            print("--------------------")
            showMonthCalendar(month, year)
            print("--------------------")
            print("Press Ctrl+C to exit")
    except KeyboardInterrupt:
        sys.exit()
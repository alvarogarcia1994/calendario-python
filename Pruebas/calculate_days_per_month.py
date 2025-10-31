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
    
print(f"Días en febrero de 2024 (bisiesto): {calculateDaysPerMonth(2, 2024)}")
print(f"Días en febrero de 2023 (no bisiesto): {calculateDaysPerMonth(2, 2023)}")
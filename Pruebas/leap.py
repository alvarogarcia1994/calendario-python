#Function to determinate if a year is leap or not
def isLeap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

#Main
def main():
    #Variable block
    year = int(input("Year: "))
    #We validate if the year is leap or not
    if isLeap(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
main()
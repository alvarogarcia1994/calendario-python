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

result = calculateDayOfWeek(1, 1, 2026)
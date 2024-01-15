tot_days = int(input())

year = 0
month = 0
day = 0
remaining = tot_days

if remaining >= 365:
    year = remaining // 365
    remaining %= 365
if remaining >= 30:
    month = remaining // 30
    remaining %= 30
    day = remaining

print(f"{year}year {month}month {day}day")
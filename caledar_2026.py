
import calendar as cal

year = 2026

print("=" * 40)
print(f"       CALENDAR OF {year}")
print("=" * 40)

for month in range(1, 13):
    print(cal.month(year, month))

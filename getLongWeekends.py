import holidays
from datetime import date, timedelta
import datetime

def get_long_weekends(year):
    us_holidays = holidays.US(years=year)
    long_weekends = []

    for date, name in sorted(us_holidays.items()):
        # print(date, name, date.weekday())
        if date.weekday() == 4:  # If holiday is on Friday
            long_weekends.append((date, date + timedelta(days=2), name))  # Weekend is till Sunday
        elif date.weekday() == 0:  # If holiday is on Monday
            long_weekends.append((date - timedelta(days=2), date, name))  # Weekend starts from Saturday

    return long_weekends

year = date.today().year # Get current year
# Get current date
current_date = datetime.date.today()

# Calculate start and end dates for past 3 months
past_start_date = current_date - datetime.timedelta(days=3*30)
past_end_date = current_date - datetime.timedelta(days=1)

# Calculate start and end dates for next 12 months
future_start_date = current_date + datetime.timedelta(days=1)
future_end_date = current_date + datetime.timedelta(days=12*30)

# Get long weekends for past 3 months
past_long_weekends = get_long_weekends(past_start_date.year)
past_long_weekends = [(start_date, end_date, holiday_name) for start_date, end_date, holiday_name in past_long_weekends if start_date >= past_start_date and end_date <= past_end_date]

# Get long weekends for next 12 months
future_long_weekends = get_long_weekends(future_start_date.year)
future_long_weekends = [(start_date, end_date, holiday_name) for start_date, end_date, holiday_name in future_long_weekends if start_date >= future_start_date and end_date <= future_end_date]

# Print long weekends for past 3 months
print("Long weekends in the past 3 months:")
for start_date, end_date, holiday_name in past_long_weekends:
    print(f"Long weekend due to {holiday_name} from {start_date} to {end_date}")

# Print long weekends for next 12 months
print("Long weekends in the next 12 months:")
for start_date, end_date, holiday_name in future_long_weekends:
    print(f"Long weekend due to {holiday_name} from {start_date} to {end_date}")
long_weekends = get_long_weekends(year)

for start_date, end_date, holiday_name in long_weekends:
    print(f"Long weekend due to {holiday_name} from {start_date} to {end_date}")

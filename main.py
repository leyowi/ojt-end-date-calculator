import datetime

hours = int(input("Number of hours of OJT: "))
input_date = input("Start of OJT (MM/DD/YYYY): ")

start_date = datetime.datetime.strptime(input_date, "%m/%d/%Y")

days_needed = (hours + 7) // 8

weekdays_count = 0

while weekdays_count < days_needed:
    if start_date.weekday() < 5:
        weekdays_count += 1
    start_date += datetime.timedelta(days=1)

end_date = start_date - datetime.timedelta(days=1)

print("Estimated End of OJT: ", end_date.strftime("%m/%d/%Y"))
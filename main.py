import datetime

input(f"[Receptionist]: Hello!...\n[You]: ")
input(f"[Receptionist]: Welcome to the py-hospital!...\n[You]: ")
input(f"[Receptionist]: What is the reason for the visit?...\n[You]: ")

first_name = input(f"[Receptionist]: Ok. For that I would need your name...\n[You]: ")
last_name = input(f"[Receptionist]: And also your last name...\n[You]: ")

date_of_birth_str = input(f"[Receptionist]: What's your date of birth? (YYYY-MM-DD)\n[You]: ")

try:
    dob = datetime.datetime.strptime(date_of_birth_str, "%Y-%m-%d").date()
    today = datetime.date.today()

    age_years = today.year - dob.year
    age_months = today.month - dob.month
    age_days = today.day - dob.day

    if age_days < 0:
        age_months -= 1
        prev_month = today.month - 1 or 12
        prev_month_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = (datetime.date(prev_month_year, prev_month % 12 + 1, 1) - datetime.timedelta(days=1)).day
        age_days += days_in_prev_month

    if age_months < 0:
        age_years -= 1
        age_months += 12
    
    next_birthday = datetime.date(today.year, dob.month, dob.day)

    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, dob.month, dob.day)

    days_until_birthday = (next_birthday - today).days

    print(f"[Receptionist]: So you're {age_years} years, {age_months} months, and {age_days} days old. And Your next birthday is in {days_until_birthday} days!")

except ValueError:
    print("[Receptionist]: Invalid date format! Please use YYYY-MM-DD.")

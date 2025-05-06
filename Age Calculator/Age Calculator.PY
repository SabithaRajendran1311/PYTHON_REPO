from datetime import datetime

# Ask user for birth date input
birth_date_input = input("Enter your birth date (YYYY-MM-DD): ")

# Convert to datetime object
birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
today = datetime.today()

# Calculate the difference
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# Adjust if the current month/day is before birth month/day
if days < 0:
    months -= 1
    days += (datetime(today.year, today.month, 1) - datetime(today.year, today.month - 1, 1)).days

if months < 0:
    years -= 1
    months += 12

# Output the result
print(f"You are {years} years, {months} months, and {days} days old.")

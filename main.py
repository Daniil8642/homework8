from datetime import datetime, timedelta, date

def get_birthdays_per_week(users):
    birthdays_by_day = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    today = date.today()
    future_birthdays_exist = False  
    if not future_birthdays_exist:
        return {}

    for user in users:
        birthday = user.get("birthday")

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
            future_birthdays_exist = True

        day_of_week = birthday.strftime("%A")

        birthdays_by_day[day_of_week].append(user.get("name"))

    
    if birthdays_by_day["Saturday"]:
        birthdays_by_day["Monday"].extend(birthdays_by_day["Saturday"])
        birthdays_by_day["Saturday"] = []

    if birthdays_by_day["Sunday"]:
        birthdays_by_day["Monday"].extend(birthdays_by_day["Sunday"])
        birthdays_by_day["Sunday"] = []


    return birthdays_by_day




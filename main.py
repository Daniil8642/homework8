from datetime import datetime, timedelta, date
from typing import List, Dict
from collections import defaultdict


def get_birthdays_per_week(users: List[Dict[str, date]]) -> Dict[str, List]:
    current_day = date.today()
    day_next_week = current_day + timedelta(days=6)

    result_dict = defaultdict(list)

    for user in users:
        name, birthday = user["name"], user["birthday"]
        birthday = birthday.replace(year=current_day.year)
        if birthday.month == 1:
            birthday = birthday.replace(year=current_day.year + 1)
        if current_day <= birthday <= day_next_week:
            if birthday.weekday() == 5 or birthday.weekday() == 6:
                result_dict["Monday"].append(name)
            else:
                result_dict[birthday.strftime("%A")].append(name)

    return result_dict

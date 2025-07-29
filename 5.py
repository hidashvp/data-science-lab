from datetime import datetime

def compare_dates(date1_str, date2_str, date_format="%Y-%m-%d"):

    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    if date1 < date2:
        return f"{date1_str} is earlier than {date2_str}"
    elif date1 > date2:
        return f"{date2_str} is earlier than {date1_str}"
    else:
        return "Both dates are the same"


date1 = "2023-07-10"
date2 = "2025-07-08"

result = compare_dates(date1, date2)
print(result)

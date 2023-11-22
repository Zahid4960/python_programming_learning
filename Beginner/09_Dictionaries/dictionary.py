make_month_conversations = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}


make_day_conversations = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday",
}


print(make_month_conversations["1"])
print(make_month_conversations.get("10"))
print(make_month_conversations.get("100"), "Not a valid key")

print(make_day_conversations["6"])
print(make_day_conversations.get("7"))
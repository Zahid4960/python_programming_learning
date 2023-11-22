def convert_month_from_params(number):
    month_to_convert = {
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

    try:
        return month_to_convert[number]
    except:
        return "Invalid params to convert month"
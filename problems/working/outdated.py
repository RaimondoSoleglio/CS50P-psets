# make the list a dictionary with corresponding numbers
months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    # check for correct input
    try:
        date = input("Date: ")
    except ValueError:
        continue
    # check for two different date formats and potential ValueError
    if "/" in date:
        try:
            month, day, year = date.split("/")
            # catching errors in the years, months and days
            if int(year) < 0 or int(month) > 12 or int(day) > 31:
                raise ValueError()
            # formatting the right output
            print("%04d-%02d-%02d" % (int(year), int(month), int(day)))
            break
        except ValueError:
            pass
    else:
        try:
            month, day, year = date.split(" ")
            # catching errors in the date format
            if "," not in day:
                raise ValueError()
            # catching errors in the years, months and days
            if int(year) < 0 or month not in months.keys() or int(day.rstrip(",")) > 31:
                raise ValueError()
            print("%04d-%02d-%02d" %
                    (int(year), months[month], int(day.rstrip(","))))  # strip and format
            break
        except ValueError:
            pass


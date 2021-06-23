# import smtplib

# myEmail = ""
# myPassword = ""

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=myEmail, password=myPassword)
#     connection.sendmail(
#         from_addr=myEmail, 
#         to_addrs="", 
#         msg="Did This Work?"
#     )


import datetime as dt

currentTime = dt.datetime.now()

year = currentTime.year
month = currentTime.month
day = currentTime.day
hour = currentTime.hour
minute = currentTime.minute
dayOfWeek = currentTime.weekday()

if year == 2021:
    print("It is 2021")

dayOfBirth = dt.datetime(year=1999, month=9, day=27)



import datetime as dt
import random
import smtplib as smtp

dayOfWeek = dt.datetime.now().weekday()

with open("quotes.txt") as file:
    quotes = file.readlines()

randomQuote = random.choice(quotes)

myEmail = ""
myPassword = ""

with smtp.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=myEmail, password=myPassword)
    connection.sendmail(
        from_addr=myEmail, 
        to_addrs="", 
        msg=randomQuote
    )

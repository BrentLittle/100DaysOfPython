from datetime import datetime
import pandas
import random
import smtplib as smtp

today = datetime.now()
today = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = { (data_row.month, data_row.day) : data_row for (index, data_row) in data.iterrows()}

myEmail = ""
myPassword = ""

if today in birthdays_dict:
    
    person = birthdays_dict[today]
    filePath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    
    with open(filePath) as letter:
        content = letter.read()
        content = content.replace("[NAME]", person["name"])

    with smtp.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=myEmail, password=myPassword)
        connection.sendmail(
            from_addr=myEmail, 
            to_addrs=person.email, 
            msg=content
        )




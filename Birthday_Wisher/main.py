import smtplib
import random

MY_EMAIL = ""
MY_PASSWORD = ""
EMAIL = ""

my_email = MY_EMAIL
my_password = MY_PASSWORD
recepient_email = EMAIL

#Getting hold of today 
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("Birthday Wisher (Day 32) start\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            #Secure it
            connection.starttls()
            #Login
            connection.login(user=my_email, password=my_password)
            #Provide sending details
            connection.sendmail(
                from_addr=my_email, 
                to_addrs="EMAIL", 
                msg=f"Subject:Monday\n\n{quote}"
            )
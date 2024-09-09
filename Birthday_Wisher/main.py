import smtplib
import random

my_email = "oleksandra.s.mukha@gmail.com"
my_password = "rvit quiq fytn jslk"

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
                to_addrs="jstivala1@babson.edu", 
                msg=f"Subject:Monday\n\n{quote}"
            )
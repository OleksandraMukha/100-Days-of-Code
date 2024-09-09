import smtplib

my_email = "oleksandra.s.mukha@gmail.com"
password = "rvit quiq fytn jslk"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="aleksamukha1535@gmail.com", 
        msg="Subject:Hello\n\nThis is a test email."
    )


#Getting hold of today 
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month

#Create daytime 
dat_of_birth = dt.datetime(year=2002, month=8, day=15)
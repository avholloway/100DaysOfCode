import pandas
import smtplib
import datetime as dt
from random import choice, randint

email_server = "mail.avholloway.com"
email_account = "anthony@avholloway.com"
email_password = "9YjfkHuuD3iRTjg"

email_subject = "Python: Testing"
email_body = """This is the body of the email.
This is line 2.

Signed,
Anthony
"""

def send_quote(quote):
    with smtplib.SMTP(email_server, port=26) as smtp_conn:
        smtp_conn.login(user=email_account, password=email_password)
        smtp_conn.sendmail(
            from_addr=email_account,
            to_addrs="anthony@avholloway.com",
            msg=f"Subject:Quote of the Day\n\n{quote}")


def send_birthday_email(to, msg):
    with smtplib.SMTP(email_server, port=26) as smtp_conn:
        smtp_conn.login(user=email_account, password=email_password)
        smtp_conn.sendmail(
            from_addr=email_account,
            to_addrs=to,
            msg=f"Subject:Happy Birthday!!!\n\n{msg}")


def wish_happy_birthday(record):
    letter = f"day32letter{randint(1, 3)}.txt"
    with open(letter) as f:
        msg = f.read()
    msg = msg.replace("[NAME]", record["name"])
    send_birthday_email(record["email"], msg)


now = dt.datetime.now()


data = pandas.read_csv("day32birthdays.csv")
for index, row in data.iterrows():
    if now.month == row["month"] and now.day == row["day"]:
        wish_happy_birthday(row)


weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
weekday = weekdays[now.day]

if False and weekday == "Monday":
    print("Today is quote sending day!")
    with open("day32quotes.txt") as f:
        quotes = [quote.rstrip() for quote in f.readlines()]
    quote = choice(quotes)
    print(f"sending the following quote:")
    print(quote)
    send_quote(quote)

import datetime as dt
import pandas as pd
import random
import smtplib
import os

now = dt.datetime.now()
today = (now.month, now.day)

df = pd.read_csv("birthdays.csv", index_col = 0)

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in df.iterrows()}

if today in birthdays_dict:
    name = birthdays_dict[today][0]
    email = birthdays_dict[today][1]
    rand_num = random.randint(1, 3)
    with open(f"letter_templates/letter_{rand_num}.txt") as file:
        data = file.read()
        replace_name = data.replace("[NAME]", name, 1)
        new_letter = replace_name
        print(new_letter)

    MY_EMAIL = os.environ.get("MY_EMAIL")
    MY_PASSWORD = os.environ.get("MY_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f'Subject:Happy Birthday!\n\n {new_letter}')

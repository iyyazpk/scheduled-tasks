##################### Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import pandas as pd
import os
now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
# datat_dict = {("month", "day"):value['month', 'day'] for key,value in data.iterrows()}
birthday_dict = {(data_row["month"], data_row["day"]): data_row for index,data_row in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as mailhub:
        mailhub.starttls()
        mailhub.login(user=my_email, password=passwd)
        mailhub.sendmail(from_addr=my_email,
                         to_addrs=my_email,
                         msg=f"From: {my_email}\nSubject: Birthday Wish\n\n{contents}")


# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)




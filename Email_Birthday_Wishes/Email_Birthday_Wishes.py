import os
import time 
import urllib.request as url
import smtplib
import schedule
import csv
import pandas as pd
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(receiver_email, subject, message):
    SENDER_EMAIL = "pratikpadman125@gmail.com"
    SENDER_PASSWORD = "maiy gyej qdil vmtu"
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(SENDER_EMAIL,SENDER_PASSWORD)

        msg = f"Subject: {subject}\n\n{message}"
        server.sendmail(SENDER_EMAIL, receiver_email, msg)
        print(f"Email sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {str(e)}")

# def load_birthday_data(file_path):
#     try:
#         file = open(file_path,'r')
#         reader = csv.DictReader(file)
#         reader = next(reader)
#         return reader
#     except Exception as e:
#         print(f"Error loading birthday data: {str(e)}")
#         return None
    
def send_birthday_wishes(email,name):
    subject = f"Happy Birthday, {name}!"
    message = f"Dear {name},\n\nHappy Birthday! We wish you a fantastic day filled with joy and laughter!\n\nBest regards,\nXYZ Company"
    send_email(email, subject, message)

def check_and_send_birthday_wishes():
    today = datetime.now().date()
    print(today)
    # reader = load_birthday_data('Birthdate.csv')
    file = open('Birthdate.csv','r')
    reader = csv.reader(file)
    next(reader,None)

    for row in reader:
        email = row[0]
        print(email)
        birthdate = datetime.strptime(row[1], "%Y-%m-%d").date()
        print(birthdate)
        
        name = email.split('@')[0]
        print(name)

        if birthdate == today:
            send_birthday_wishes(email, name)
        


def main():
    try:
        # Schedule the task to run daily at a specific time(12:00AM)
        schedule.every().day.at("12:00").do(check_and_send_birthday_wishes)

        # Main loop to keep the script running
        while True:
            schedule.run_pending()
            time.sleep(1)
    except Exception as E:
        print(E)


if __name__ == "__main__":
    main()
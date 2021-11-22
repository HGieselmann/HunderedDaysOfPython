import datetime as dt
import smtplib
import pandas as pd

birthdays = pd.read_csv("birthdays.csv")
month_and_day = birthdays[["month", "day"]]
month_and_day

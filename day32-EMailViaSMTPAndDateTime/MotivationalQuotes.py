import random
import smtplib
import datetime as dt

email = "test@test.com"
password = "UltraSecurePassword"


def get_motivational_quote():
    with open("motivationalQuotes") as file:
        content = file.readlines()
        return random.choice(content)


def send_mail(mailtext):
    dummy = True
    if dummy:
        print(mailtext)
        print("Mail send.")
    else:
        with smtplib.SMTP("smtp.domain.com") as connection:
            connection.startttls()
            connection.login(user=email, password=password)
            connection.sendemail(
                from_addr=email,
                to_addrs="targetmail@domain.com",
                msg="Subject:My Subject\n\nMail body text.")


today = dt.datetime.now()
if today.weekday() == 0:
    motivaional_quote = get_motivational_quote()
    send_mail(motivaional_quote)

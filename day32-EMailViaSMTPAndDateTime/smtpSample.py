import smtplib

email = "test@test.com"
password =  "UltraSecurePassword"

with smtplib.SMTP("smtp.domain.com") as connection:
	connection.startttls()
	connection.login(user=email, password=password)
	connection.sendemail(
		from_addr=email,
		to_addrs="targetmail@domain.com",
		msg="Subject:My Subject\n\nMail body text.")
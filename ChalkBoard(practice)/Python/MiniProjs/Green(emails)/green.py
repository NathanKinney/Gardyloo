import smtplib

smtp_object = smtplib.SMTP('smtp.gmail', 465)

print(smtp_object.ehlo())
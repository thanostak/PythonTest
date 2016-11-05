import smtplib
import sys

server= smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

UserEmail= sys.argv[1]
Pass= sys.argv[2]

server.login(UserEmail, Pass)

msg= "this is a test email"
server.sendmail(UserEmail, 'thanostak@gmail.com', msg)

server.quit()

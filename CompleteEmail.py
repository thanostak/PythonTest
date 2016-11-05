import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import sys
filename= 'C:/Users/tsako/Desktop/useremails.txt'
# try to parse the .txt file and place the values in a dict 

try:
	with open(filename) as f:
		for line in f:
			parts= line.strip().split(';')
			for n in range(1):
				UserEmail= parts[0]
				Pass= parts[1]
				 
except EnvironmentError:
	print "Wrong filename"
	

# UserEmail= sys.argv[1]
# Pass= sys.argv[2]


toaddr= "thanostak@gmail.com"
msg= MIMEMultipart()
msg['From']= UserEmail
msg['To']= toaddr
msg['Subject']= "einai iperoxo"
body= "ayto einai apla ena test"
msg.attach(MIMEText(body, 'plain'))

server= smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(UserEmail, Pass)
text= msg.as_string()
server.sendmail(UserEmail, toaddr, text)
server.quit()

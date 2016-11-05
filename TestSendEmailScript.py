import smtplib
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


server= smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(UserEmail, Pass)

msg= "this is a test email"
server.sendmail(UserEmail, 'thanostak@gmail.com', msg)

server.quit()

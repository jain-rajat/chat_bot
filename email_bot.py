import smtplib

import config

def send_email(email1,msg):


	try:
		

		final='\n Booking confirmed:  no. of person=' + str(msg['person']) + ' Date= ' +msg['date'] +'Time='+msg['time']
		mail=smtplib.SMTP('smtp.gmail.com',587)
		mail.ehlo()
		mail.starttls()
		mail.login(config.email_id,config.passw)
		mail.sendmail(config.email_id,email1,final)
		mail.quit()
		return 'Check Your mail for booking confirmation'
	except:
		return 'Mail sent failure'


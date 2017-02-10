import smtplib

def send_email(from_name, from_email, subject, msg):
	#from_addr = {}
	to_addr  = 'g@gmail.com'
	# from_name = {}
	to_name = 'Georgia Pickersgill'
	subject = {}
	msg = {}
	message = """From: {} <{}>
	To: {} <{}>
	Subject: {}
	{}
	"""

	message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)
	# Credentials (if needed)
	username = 'g@gmail.com'
	password = 'j'
	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(from_addr, to_addr, message_to_send)
	server.quit()
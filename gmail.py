import smtplib
import csv
import datetime


class Gmail:

	def send_email(self, to_email, msg, subject, user):

	    from_address = user.email     # 'gtestigwe@gmail.com'
	    to_address = to_email

	    subject = subject
	    msg  = 'Subject: {}\n\n{}'.format(subject, msg)

	    password = user.password #password goes here

	    try:
	       
	        with open('messages.csv', 'a') as file:
	        	messages= csv.DictWriter(file, fieldnames=['from', 'to', 'message', 'timestamp'])
	        	messages.writerow({'from': from_address, 'to': to_address, 'message': msg, 'timestamp': datetime.now() }) 

	        print('Message sent successfully to {}'.format(email))
	      
	    except Exception as e:
	        print('Sorry email was not sent, Try again', e)

	def compose_email(self, message='', to='', subject=''):
			subject = input('Please enter subject: ')
			message = input("Compose new message here: ")
			to = input('Enter email address: ')
			self.send_email(to, message, subject)

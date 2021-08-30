from email.message import Message
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

 ##Update username and password


def sendmail(mailid,results):
	sender_address = 'tarunm.dml23@iiitb.net'
	sender_pass = 'Mar@2021'	
	receiver_address = mailid
	print(receiver_address)
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address  #The subject line
	
	size:int = 10 if 10< results.shape[0] else results.shape[0] 	
	message['Subject'] = F'Top {size} restaurants search results' 
	mail_content= F"Found below top {size} restaurants \n"
	for restaurant in results.iloc[:5].iterrows():
		restaurant = restaurant[1]
		mail_content=mail_content + F"Restaurant Name: {restaurant['Restaurant Name']} \n Restaurant locality address {restaurant['Address']} \n Average budget for two people {restaurant['Average Cost for two']} \n Zomato user rating {restaurant['Aggregate rating']} \n  \n\n"
	
	message.attach(MIMEText(mail_content, 'plain'))
	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	return "Mail sent"

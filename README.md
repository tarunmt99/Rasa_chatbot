Upgrad RASA Restaurent search chatbot

below are the pre-requitse packages required

rasa[spacy]==2.8.2
spacy download en_core_web_md

For the email functionality update the credentails 'send_email.py'

	sender_address = '' # username
	sender_pass = '' #password	
        
To run the chatbot in the interactive mode below 2 commands shoule be run in two different windows

        rasa shell #1st window
        rasa run actions # 
        
 Sample email from chatbot is attached in the root folder
 
 

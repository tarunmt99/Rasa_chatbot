# Import the email modules we'll need
from email.parser import BytesParser, Parser
from email.policy import default

# If the e-mail headers are in a file, uncomment these two lines:
# with open(messagefile, 'rb') as fp:
#     headers = BytesParser(policy=default).parse(fp)

#  Or for parsing headers in a string (this is an uncommon operation), use:
def sendmail(receipent, response):
    headers = Parser(policy=default).parsestr(
            'From: Foo Bar <user@example.com>\n'
            'To: '+receipent+'\n'
            'Subject: Test message\n'
            '\n'
            'Body would go here\n')

    #  Now the header items can be accessed as a dictionary:
    print('To: {}'.format(headers['to']))
    print('From: {}'.format(headers['from']))
    print('Subject: {}'.format(headers['subject']))


class Notification:
    def __init__(self,email_id):
        self.email_id=email_id
        
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print(f'Emailnotification {email_id}  has been sended.')
        
class SMSNotification(Notification):
    def send(self):
        print(f'Sms notification {mobile_no} has been sended')

email_id=input("Enter email id : ")
mobile_no=int(input("enter mobile number: "))

emailnotification=EmailNotification(email_id)
emailnotification.send()

smsnotification=SMSNotification(mobile_no)
smsnotification.send()


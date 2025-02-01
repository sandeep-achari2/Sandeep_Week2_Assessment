

class Logger():    
    def log(self,messages,lower_message="info"):
        if lower_message=="error":
            print(f'{messages} message is {lower_message}')
        elif lower_message=="warning":
            print(f'{messages} message is {lower_message}')
        elif lower_message=="info":
            print(f'{messages} message is {lower_message}')
        else:
            print("Enter correct log message")

messages=input("enter message: ")
lower_msg=input("Enter string or lower msg: ")
logger=Logger()
logger.log(messages,lower_msg)


class Payment():
    def process_payment(self,amount):
        pass
    
class CreditCardPayment(Payment):
    def process_payment(self,amount):
        return f'Creditcardpayement {amount} sucessful'
    
class PayPalPayment(Payment):
    def process_payment(self, amount):
        return f'Paypalpayment {amount} sucesssful'
    
class BitCoinPayment(Payment):
    def process_payment(self, amount):
        return f'Bitcoinpayment {amount} sucessful'
    
amount1=float(input("Enter amount for credircardpayment: "))
amount2=float(input("Enter amount for paypalpayment: "))
amount3=float(input("Enter amount for Bitcoinpayment: "))
creditcard=CreditCardPayment()
print(creditcard.process_payment(amount1))

paypal=PayPalPayment()
print(paypal.process_payment(amount2))

bitcoin=BitCoinPayment()
print(bitcoin.process_payment(amount3))


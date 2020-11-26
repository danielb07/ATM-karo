class ATM:
    def __init__(self,cardNo,pin):
        self.cardNo = cardNo
        self.pin = pin

    def CashWithdrawl(self):
        print(self.cardNo)

    def BalanceEnquiry(self):
        print(self.pin)     

CardNo = input('Please write your card number here: ')    
Pin = input('Please write your pin here: ')    

atm = ATM(CardNo,Pin)
atm.CashWithdrawl()
atm.BalanceEnquiry()
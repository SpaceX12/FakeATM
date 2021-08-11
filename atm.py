class Atm:
    def __init__(self,):
        self.cNo = input('Enter Your Credit Card Number:')
        self.pNo = input('Enter Your Credit Card Pin:')

    def cashWD(self,):
        self.wD = input('Cash Withdrawal of:')
        print(self.wD) 

    def saveCash(self):
        self.sC = input('Save an amount of:')
        print(self.sC)

bnk = Atm()
getCash = bnk.cashWD()
save = bnk.saveCash()
class GrandParent():
    def __withdrawlMoney(self,bankName,accountNumber,atmPin):
        self.bankName = bankName
        self._accountNumber = accountNumber
        self.__atmPin = atmPin
        print('Withdrawl monry by GrandParent')

    def _UpdatePassBook(self):
        print('Update the passbook ')

class Parent(GrandParent):
    def chequePayment(self):
        print("Withdraw money by Parent")

class GrandSon(Parent):
    def UpdatePassBook(self):
        print('Update Passbook')

g = GrandSon()
#g.__withdrawlMoney()  #this is not accessible becuase it is Private
g._UpdatePassBook(1000235)   #this is accessible becuse it is Protected and it is within main class
print(bankcode)
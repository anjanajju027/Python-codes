# loan approval
# loan rejection
# approved loan request
import pytest
@pytest.mark.smoke

class loan():
    def json_file(self,file,data):
        self.file = file
        self.data = data
        with open(('file_name','w') as json_file:
        data = json_file.load (json_file)
        return data

    def file_open(self,file,read):
        self.read = read
        self.file = file
        with open ('file_name','r') as json_file:
         read = json_file.load(json_file)
         return read



    name = 'anjan'
    def __init__(self,credit,anuual_income):
        self.credit = credit
        self.anuual_income = anuual_income

        if self.credit <6000:
            return "credit is low"
        if self.anuual_income <= 10000:
            return "annual is low"
        else:
            return "loan approoved"

a1 = loan()
a1.loan(6000,7000)


def loan_approval(credit, anuual_income):
     pass


@pytest.mark.smoke
def test_loan_reject():
    credit = 5000
    anuual_income = 1000
    result = loan_approval(credit,anuual_income)
    assert result== "loan is approved"


@pytest.mark.smoke
def test_creditscore():
    credit = 90000
    annual_income = 61000
    result = loan_approval(credit,annual_income)
    assert  result == "rejected due to high amount"




class Loan:
    def __init__(self, credit, annual_income):
        self.credit = credit
        self.annual_income = annual_income
        self.loan_status = self.check_loan_status()

    def check_loan_status(self):
        if self.credit < 6000:
            return "credit is low"
        if self.annual_income <= 10000:
            return "annual income is low"
        return "loan approved"


a1 = Loan(6000, 7000)
print(a1.loan_status)  # Output: loan approved

@pytest.mark.smoke
def test_loan_reject():
    credit = 5000
    annual_income = 1000
    result = Loan(credit, annual_income).loan_status
    assert result == "credit is low"

@pytest.mark.smoke
def test_creditscore():
    credit = 90000
    annual_income = 61000
    result = Loan(credit, annual_income).loan_status
    assert result == "loan approved"

















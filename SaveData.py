from simple_salesforce import Salesforce
import csv
import os

directory = os.getcwd()

Cusername = ""
Cpassword = ""
Ctoken = ""

def Creds(username, password, token):
    Cusername=username
    Cpassword=password
    Ctoken=token

    sf = Salesforce(
        username=Cusername,
        password=Cpassword,
        security_token=Ctoken
    )


def UploadData(text):
        reader = csv.reader(text)
        items = list(reader)

        org_name = items[0][0]
        weight_sum = 0

        for i in range(1, len(items[0])):
            weight_sum += float(items[0][i])

        acquisition_values = {
            "Account__c": org_name,
            "Weight__c": weight_sum,
            "Tapin_Expense__c": "0"
        }

        sf.Acquisition__c.create(acquisition_values)

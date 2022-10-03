import json
import requests
import csv

base_url = 'https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest'
header = {"x-api-key" : 'qaEMpgfPNC4wvRuApSEiD7HzNRGrKTkd1yBFiwXP'}

resp = requests.post(base_url, header).json()
dataToImport = resp['customer']
dataToImport1 = resp['loaninfo']

with open('app.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['firstname', 'lastname', 'address1', 'addresss2', 'city', 'state', 'zipcode'])
    writer.writerow(dataToImport.values())
    writer.writerow(['original_amount_financed', 'current_principal_balance', 'current_interest_balance', 'current_fees_balance', 'current_late_charge_balance', 'current_payoff_balance', 'next_due_date'])
    writer.writerow(dataToImport1.values())
        
# print(dataToImport)
# print(resp)
print('done')


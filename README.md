# AvidCodeTest
Simple Code Test

Create a proper python script that calls the api method = POST

Take the results and create a csv file

All data returned in api call should be on one line in the csv file with the fields returned as the header
for example:


{"field1":value1,"field2":value2} 

should be

field1, field2
value1,value2

The Api call that will return your data is:
https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest

ApiKey is in the .env file
Pass the apikey to the call by using the header x-api-key

Questions: 
Why is is bad practice to include the .env file in a git repository?
What file would you create in a git repository to make sure that this file was not included?

To complete the assignment:

Use git commands to do the following:

Clone the repository to your local development computer
Create the program in the app.py file in the repository
Commit your changes
Upload the file to the github repository with your firstname_customerloan.csv firstname being your first name
Create a pull request

To help you get started, here is a CURL example:

curl --location --request POST 'https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest' \
--header 'x-api-key: qaEMpgfPNC4wvRuApSEiD7HzNRGrKTkd1yBFiwXP' \
--data-raw ''

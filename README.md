# AvidCodeTest
<b>Simple Code Test</b>

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

<b>Questions: </b></br>
Why is is bad practice to include the .env file in a git repository?
What file would you create in a git repository to make sure that this file was not included?

To complete the assignment:

Use git commands to do the following:

Fork a copy of this repository into your git hub account
Clone the repository to your local development computer
Create a branch using the Git Checkout command
Create the program in the app.py file in the repository
Commit your changes and push this branch to your repository
Upload the csv file to the github repository with your firstname_customerloan.csv firstname being your first name
Send me the link to your repository (ahill@avidac.com)

To help you get started, here is a CURL example:

curl --location --request POST 'https://mko2aswez1.execute-api.us-west-2.amazonaws.com/V1/AvidCodeTest' \
--header 'x-api-key: qaEMpgfPNC4wvRuApSEiD7HzNRGrKTkd1yBFiwXP' \
--data-raw ''

<b>Stretch Goal</b></br>
Send me an email and let me know if you would like to attempt this. (ahill@avidac.com)
Once you send a request to try this challenge I will send you the access key and secret key to use for your AWS profile
You will need to install the AWS Sdk and then issue a aws configure command.  It will ask you some questions.
  
The AWS Access Key ID is the Access Key I will send you.
The AWS Secret Access Key is the Secret Key I will send you.
The Default region name is us-west-2
The Default output format is json

You now have a credentials file on your machine with a profile in it representing the information you input above.
See https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html for more information

Use the requirements file in the repository to install Boto3
Write a method in the project that will send me an email using AWS Simple Notification Service or SNS.
In the body of the email, send me the contents of the api call.




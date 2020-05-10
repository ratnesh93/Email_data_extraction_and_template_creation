"""
Author: Ratnesh Chandak
versions:
    Python 3.7.4
    pandas==0.25.1
"""

import pandas as pd

#reading input file 
data=pd.read_csv("sample_email.csv",encoding='latin1')

#taking user input for adding user define name in email template
user_Defined_Name=input().strip()

#creating email template
template=pd.Series("Email to :"+data['email']+"\n"+\
    "Subject Line :"+data['subject']+"\n"+\
    "Hi "+data['first_name']+" "+data['last_name']+",\n"+\
    data['Email Boby']+"\n"+\
    "Please do contact me at "+data['phone']+"\n"+\
    "Thanks,\n"+\
    user_Defined_Name)

#sample template showing to user
print("-------------------printing sample template------------------")
print(template[0])

#creating dataframe to save email template correponding to each email id
email_template = pd.DataFrame(columns=['to_mail','template'])
email_template.to_mail=data['email']
email_template.template=template

#saving email template to email_template.csv
email_template.to_csv('email_template.csv',index=False)

#creating dataframe to save number and email from email body corresponding to each email id
dfExtractedObj = pd.DataFrame(columns=['to_email','extracted_number','extracted_email'])
dfExtractedObj.to_email=data['email']
dfExtractedObj.extracted_number=data['Email Boby'].str.extract(pat='(\d{3}-\d{3}-\d{4})',expand=False)
dfExtractedObj.extracted_email=data['Email Boby'].str.extract(pat='([\w]+@[\w.]+)',expand=False)

#saving extracted email and number to another csv file
dfExtractedObj.to_csv('extracted_Phone_email.csv',index=False,na_rep="----")
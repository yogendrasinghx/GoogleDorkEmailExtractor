import requests
import bs4	
import re
import sys


#Command line argument for input file 
#filename = sys.argv[1]
filename = "email_dork.csv"

#List for storing emails
emails = []

#Regex for email
email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

#Get dork query from file
with open(filename, 'r') as file:
    raw_line = file.readlines()
    
#Removing new line from raw_line    
dork_query = [query.split("\n")[0] for query in raw_line]


#Loop for extracting emails for google search results
for query in range(5):  #change it with "for query in dork_query:"

    #Accepts Search Keywords from the User
    keyword = dork_query[query]

    #Setting Query Parameters for Search 
    params = [('q',keyword)]

    #Google Search URL
    url = "https://google.co.in/search"

    # Gets response from the server for the search query
    response = requests.get(url=url, params=params)

    # Response text from server is parsed using bs4
    soup = bs4.BeautifulSoup(response.text,'html.parser')

    #Extracting emails from the response
    for i in soup('div'):
        #print(i.get_text())
        match = re.findall(r'[\w\.-]+@[\w\.-]+', i.get_text())
        for dist in match:
            emails.append(dist)

    #Remove duplicates
    emails = list(set(emails))


#Remove duplicates
emails = list(set(emails))

#Printing result to console
for i in emails:
    print(i)
    
#Writing emails to Emails.txt file
if len(emails)>0:
    with open("Emails.txt", 'w') as file:
        for email in emails:
            file.write(email+"\n")
    






import requests
import bs4	
import re
import sys
from random import randint
from time import sleep

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

c = 0

#Loop for extracting emails for google search results
for query in dork_query:  #change it with "for query in dork_query:"

    print(c+1)

    c = c + 1
    
    #Accepts Search Keywords from the User
    keyword = query

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
            if dist[len(dist)-1]==".":
                dist = dist[:len(dist)-1]
            emails.append(dist)
            #print(dist)
            #with open("Emails.txt", 'w') as file:
                #file.write(dist+"\n")
                

    #Remove duplicates
    emails = list(set(emails))
    print(emails)
    with open("raw_emails.txt", 'w') as file:
        for email in emails:
            file.write(email+"\n")
                       
    #Cooldown time
    sleep(randint(10,100))

    '''#Printing result to console
    for i in emails:
        print(i)'''


#Remove duplicates
emails = list(set(emails))

  
#Writing emails to Emails.txt file
if len(emails)>0:
    with open("dist_emails.txt", 'w') as file:
        for email in emails:
            file.write(email+"\n")

    






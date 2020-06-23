import requests
import bs4	
import re

emails = []

email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

#Accepts Search Keywords from the User
keyword = 'site:twitter.com -inurl:(search|favorites|status|statuses|jobs) -intitle:(job|jobs) -recruiter -HR -careers "New Hampshire" "gmail.com" "actor"'

#Setting Query Parameters for Search 
params = [('q',keyword)]

#Google Search URL
url = "https://google.co.in/search"

# Gets response from the server for the search query
response = requests.get(url=url, params=params)

# Response text from server is parsed using bs4
soup = bs4.BeautifulSoup(response.text,'html.parser')


#spans = soup.findAll("div", {"class": "st"})

for i in soup('div'):
    #print(i.get_text())
    match = re.findall(r'[\w\.-]+@[\w\.-]+', i.get_text())
    for dist in match:
        emails.append(dist)

#Remove duplicates
emails = list(set(emails))

for i in emails:
    print(i)

#[soup('div')[i].get_text() for i in range(10,30)])

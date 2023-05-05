from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://registrar.web.baylor.edu/exams-grading/spring-2023-final-exam-schedule'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

myclasses = ['MW 2:30 p.m.']

classes_list = soup.findAll('tr')

for c in classes_list:
    final = c.findAll('td')
    if final: #means there is something in there
        myclass = final[0].text
        if myclass in myclasses:
            print(f"For class: {myclass} the final is scheduled for {final[1].text} at {final[2].text}")


        




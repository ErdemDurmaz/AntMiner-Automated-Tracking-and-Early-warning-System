import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
from base64 import b64encode
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#READER CODE IMPLEMENT IT LATER
#url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')
#count = 0
# Retrieve all of the anchor tags
#tags = soup('a')
#miners local ip

#future code:refactor it!
'''
page = requests.get("http://192.168.0.108/cgi-bin/minerStatus.cgi")
soup = BeautifulSoup(page.content, 'html.parser')
warning = soup.find(id="degreet")
mineritems = seven_day.find_all(class_="tombstone-container")
degree = forecast_items[0]
print(degree.prettify())
    while true"
    if degree > 80:
        print("Warning",warning)
        usrinp =inp("Press p to quit")
        if usrinp  == q:
            quit()
'''
# import requests
# url = 'http://internet.iitb.ac.in/index.php'
# values = {'uname': '17B030008',
#           'passwd': 'hihello123@',
#           "value" : "Login"}

# r = requests.post(url, data=values)
# print (r.content)

import time

time.sleep(60)

from robobrowser import RoboBrowser
browser = RoboBrowser()
login_url = 'my_url'
browser.open('http://internet.iitb.ac.in/index.php')
form = browser.get_form()
print(form)
form["uname"].value = "17B030008" 
form["passwd"].value = "hihello123@"
print(form)
browser.submit_form(form)
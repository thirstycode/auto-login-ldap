import time

time.sleep(60)

from robobrowser import RoboBrowser
browser = RoboBrowser()
login_url = 'my_url'
browser.open('http://internet.iitb.ac.in/index.php')
form = browser.get_form()
print(form)
form["uname"].value = "" 
form["passwd"].value = ""
print(form)
browser.submit_form(form)

# auto-login-ldap-internet (Only for IITB lan)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/) &nbsp;&nbsp; [![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)<br>
<br>

**Automatic login in ldap if you don't have screen to your raspberry pi. Only one time setup 😃**

### Installation:

```bash
1. git clone https://github.com/thirstycode/auto-login-ldap-internet
2. cd auto-login-ldap-internet
3. pip3 install robobrowser
```
4. Add username and password to main_all.py

#### Execute It:
```bash
1. python main_all.py
```
#### Adding Cron Job To Execute It Every  Reboot:
```bash
1. @reboot python /home/pi/auto-login-ldap-internet/main_all.py
(This path can be different for everyone)
```

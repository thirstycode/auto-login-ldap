# auto-login-ldap
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)<br>
<br>

**Automatic login in ldap if you don't have screen to your raspberry pi. Only one time setup 😃**

### Installation:

```bash
1. git clone https://github.com/thirstycode/auto-login-ldap-internet
2. cd auto-login-ldap-internet
3. pip3 install selenium
```
4. Add username and password to main.py

#### Execute It:
```bash
1. python main.py
```
#### Adding Cron Job To Execute It Every  Reboot:
```bash
1. @reboot python /home/pi/auto-login-ldap-internet/main.py
(This path can be different for everyone)
```

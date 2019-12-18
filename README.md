### Python Cron alerting using AWS SES to send an email on status code !200.
### This is needed for the mission-critical cron health check.

```
0 0 * * * /usr/bin/python /path/to/cron-en.py <URL for cron>
```

### Please edit the from_address, to_address, name, server, server.login in the cron-en.py file as per your env.

This script will read $1 and tested against python 2 and 3 and using all default modules expect requests which can be installed as below.

```
pip install requests
```

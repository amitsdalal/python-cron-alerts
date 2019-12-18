### Python Cron alerting using AWS SES to send email on status code !200.
### This is needed for mission crtical cron health check.

```
0 0 * * * /usr/bin/python /path/to/cron-en.py <URL for cron>
```

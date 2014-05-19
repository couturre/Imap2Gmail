"""
Copyright (c) Pier-Luc Brault
plbrault@gmail.com

This file is part of Imap2Gmail.
Please read LICENSE.txt for complete copyright and license notice.
"""

from imap_fetcher import ImapFetcher
import smtplib
from datetime import datetime
import settings


def log(text):
    """Print a string to system output with current date and time"""
    print("[%0s] %1s" % (datetime.now().isoformat(), text))


###### MAIN ######

log("************************************")
log("A new execution begins")

# Settings file validation
log("Validating settings file")
valid_settings = True
if not hasattr(settings, 'IMAP_ACCOUNTS'):
    log("IMAP_ACCOUNTS setting is missing")
    valid_settings = False
    pass
elif not hasattr(settings, 'MAIL_TO'):
    log("MAIL_TO setting is missing")
    valid_settings = False
    pass
elif not hasattr(settings, 'SMTP_SERVER'):
    log("SMTP_SERVER setting is missing")
    valid_settings = False
    pass
elif type(settings.IMAP_ACCOUNTS) != list:
    log("IMAP_ACCOUNTS setting must be a list")
    valid_settings = False
elif type(settings.MAIL_TO) != str:
    log("MAIL_TO setting must be a string")
    valid_settings = False
elif type(settings.SMTP_SERVER) != dict:
    log("SMTP_SERVER setting must be a dictionary")
    valid_settings = False
elif ("host" not in settings.SMTP_SERVER 
        or "port" not in settings.SMTP_SERVER
        or type(settings.SMTP_SERVER["host"]) != str
        or type(settings.SMTP_SERVER["port"]) != int):
    log("SMTP_SERVER setting is not formatted correctly")
    valid_settings = False
else:
    for account in settings.IMAP_ACCOUNTS:
        if ("host" not in account 
                or "port" not in account 
                or "login" not in account 
                or "password" not in account 
                or "ssl" not in account
                or type(account["host"]) != str
                or type(account["port"]) != int
                or type(account["login"]) != str
                or type(account["password"]) != str
                or type(account["ssl"]) != bool):
            log("IMAP_ACCOUNTS setting is not formatted correctly")
            valid_settings = False
            break

# If settings file is valid, proceed.
if valid_settings:
    log("Settings file validation passed")
    
    smtp = smtplib.SMTP(settings.SMTP_SERVER["host"], settings.SMTP_SERVER["port"])
    
    for imap_account in settings.IMAP_ACCOUNTS:
        fetcher = ImapFetcher()
    
        log("Connecting to IMAP account %0s at host %1s" % (imap_account["login"], imap_account["host"]))
        try:
            fetcher.open_connection(imap_account['host'], imap_account['port'], imap_account['login'], imap_account['password'], ssl=imap_account['ssl'])
        except Exception as e:
            log("Connection failed : %1s" % (e))
            continue
        
        log("Fetching unread messages")
        messages = fetcher.fetch_new_messages()
        log("%0i message(s) fetched" % (len(messages)))
        
        log("Closing connection")
        fetcher.close_connection()
    
        for message in messages:
            log('Transferring message "%0s" from %1s' % (message["Subject"], message["from"]))
            try:
                smtp.sendmail(message["from"], settings.MAIL_TO, message.as_string())
            except Exception as e:
                log("Message sending failed: %0s" % (e))
                
    smtp.quit()
    log("Execution is completed")
    
# If settings file is invalid, terminate.
else:
    log("Settings file validation failed. Terminate.")

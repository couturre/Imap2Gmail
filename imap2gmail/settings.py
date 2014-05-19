# This file contains the settings used by Imap2Gmail
# to retrieve mail from IMAP accounts and transfer them
# to a given email address.


# Information of the IMAP accounts to retrieve mail from
IMAP_ACCOUNTS = [
                    {
                        'host':'',
                        'port':993,
                        'login':'',
                        'password':'',
                        'ssl':False
                    },
                 ]                          
# Email address to wich the retrieved messages will be transferred
MAIL_TO = ""
# SMTP Server to use for the transfer
SMTP_SERVER = {'host':"", 'port':25}

# Nothing to change passed this line


try:
    settings_dev = __import__("settings_dev")
    IMAP_ACCOUNTS = settings_dev.IMAP_ACCOUNTS
    MAIL_TO = settings_dev.MAIL_TO
    SMTP_SERVER = settings_dev.SMTP_SERVER
except:
    pass
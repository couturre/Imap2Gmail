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


smtp = smtplib.SMTP(settings.SMTP_SERVER["host"], settings.SMTP_SERVER["port"])

for imap_account in settings.IMAP_ACCOUNTS:

    # Fetch new messages
    fetcher = ImapFetcher()
    fetcher.open_connection(imap_account['host'], imap_account['port'], imap_account['login'], imap_account['password'], ssl=imap_account['ssl'])
    messages = fetcher.fetch_new_messages()
    fetcher.close_connection()

    # Transfer fetched messages
    emails_transferred = 0
    for message in messages:
        smtp.sendmail(message["from"], settings.MAIL_TO, message.as_string())
        emails_transferred += 1
    print("{0} messages transferred [{1}]".format(emails_transferred, datetime.now()))
            
smtp.quit()

Imap2Gmail
Copyright (c) 2014 Pier-Luc Brault
plbrault@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

Please read LICENSE.txt for complete license notice.

***


EXECUTION ENVIRONMENT

Python 3.4

***


To use this program, supply needed information in settings.py file, and
add a crontab entry to execute « python3 imap2gmail.py » regularly.

You can use an output redirect for logging purpose, 
e.g. « python3 imap2gmail.py > /var/log/imap2gmail.log ».
Make sure that the log file exists and is writable.
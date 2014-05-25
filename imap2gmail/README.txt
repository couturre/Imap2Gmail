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

Python 3.x

***


To use this program, supply needed information in settings.py file, and
add a crontab entry to execute it regularly. You can also use an output
redirection for logging purpose.
 
Crontab entry example to run imap2gmail every 15 minutes and log its output: 
*/15 * * * * /usr/bin/python3 /usr/imap2gmail/imap2gmail.py > /var/log/imap2gmail.log
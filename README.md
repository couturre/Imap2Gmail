# Imap2Gmail

This program fetches all unread messages from the given IMAP accounts, and transfers them
to the given email address. It is useful for fetching mail from IMAP accounts into Gmail.

## Requirements

* Python 3.x

## Setup

Supply needed information in settings.py file, and
add a crontab entry to execute it regularly. You can 
also use an output redirection for logging purpose.
 
### Crontab entry example

    */15 * * * * /usr/bin/python3 /usr/imap2gmail/imap2gmail.py > /var/log/imap2gmail.log

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
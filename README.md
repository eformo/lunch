# lunch
## About
For those that are stuck in an office with people that can't get a lunch ordered and called in.
## Instructions to run script
1. Create a list of people in your office using the same format as example.in
2. Modify the filename of the list in the script
3. Download an image to send with your email  

## Instructions to setup mutt with gmail
1. Install Mutt  
`sudo apt-get install mutt`
2. Create new gmail address
3. enable IMAP
4. enable less-secure devices - https://support.google.com/accounts/answer/6010255?hl=en
5. edit the ~/.muttrc file
```
set imap_user = "<your_email>@gmail.com"
set imap_pass = "<your_password>"

set smtp_url = "smtp://<your_email>@smtp.gmail.com:587/"
set smtp_pass = "<your_password>"
set from = "<your_email>@gmail.com"
set realname = "Lunch_Boss"

set folder = "imaps://imap.gmail.com:993"
set spoolfile = "+INBOX"
set postponed="+[Gmail]/Drafts"

set header_cache=~/.mutt/cache/headers
set message_cachedir=~/.mutt/cache/bodies
set certificate_file=~/.mutt/certificates

set move = no
```

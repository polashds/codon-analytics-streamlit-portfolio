
import imaplib
import email
import pandas as pd
import re

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('your_email@gmail.com', 'password')
mail.select('inbox')

status, messages = mail.search(None, 'ALL')
email_ids = messages[0].split()

data = []
for e_id in email_ids[:10]:
    _, msg = mail.fetch(e_id, '(RFC822)')
    msg_content = email.message_from_bytes(msg[0][1])
    body = msg_content.get_payload(decode=True).decode()
    match = re.search(r'Total:\s*\$([0-9\.]+)', body)
    if match:
        data.append({'email_id': e_id, 'total': match.group(1)})

df = pd.DataFrame(data)
df.to_csv('email_data.csv', index=False)
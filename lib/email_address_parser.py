import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses
    def parse(self):
        emails = re.split(r'\s|,|[\s,]+', self.addresses)
        new_emails = []
        for e in emails:
            if len(e) > 0 and '@' in e:
                new_emails.append(e)
        new_emails.sort()
        return new_emails
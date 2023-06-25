#!/usr/bin/env python3

from email_address_parser import EmailAddressParser

if __name__ == '__main__':
    parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
    parser.parse()
    import ipdb; ipdb.set_trace()

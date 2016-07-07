import re

# Pandas email column extraction code comes here. All emails
# extracted is put into inputemails list.

inputemails = ['thechristian@versified.xyz.gh', 'gdg']        # Emails from uploaded file. Email key would be used to test each entry.
validemail = []         # will contain entries that pass as a valid email
invalidemail = []       # will contain entries that does not pass as a valid email
emailkey = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

def emailvalidator():
    for email in inputemails:
        checkemail = re.search(emailkey, email)
        if checkemail:
            matchemail = checkemail.group()
            validemail.append(matchemail)
        else:
            invalidemail.append(email)

emailvalidator()
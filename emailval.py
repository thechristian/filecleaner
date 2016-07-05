import re

invalidemail = []
emailkey = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
matchemail = re.search(emailkey, 'thechristian@versified.xyz.gh')
validemail = matchemail.group()
if matchemail:
    print validemail
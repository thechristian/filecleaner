import re
import pandas as pd
from utils import get_random_id

validemail = []         # will contain entries that pass as a valid email
invalidemail = []     # will contain entries that does not pass as a valid email
emailkey = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
phonenumbkey = "regex expression"


def emailvalidator(fname, sname, colname):
    data = pd.read_excel(fname, sname)
    df = pd.DataFrame(data)
    if colname in df:
        emails = df.loc[:, colname]
        for email in emails:
            checkemail = re.search(emailkey, email)
            if checkemail:
                matchemail = checkemail.group()
                validemail.append(matchemail)
                writer = pd.ExcelWriter('emails/validEmails-' + get_random_id() + '.xlsx', engine='xlsxwriter')
                dataframe = pd.DataFrame(validemail, columns=["Valid Emails"])
                dataframe.to_excel(writer, sheet_name=sname, index=False)
                writer.save()
            else:
                invalidemail.append(email)
                writer = pd.ExcelWriter('emails/invalidEmails-' + get_random_id() + '.xlsx',  engine='xlsxwriter')
                dataframe = pd.DataFrame(invalidemail, columns=["Invalid Emails"])
                dataframe.to_excel(writer, sheet_name=sname, index=False)
                writer.save()
    else:
        return "Column name does not exist"


def phonenumbvalidator():
    print "phone number validation code"

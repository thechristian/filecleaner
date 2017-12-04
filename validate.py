import os
import re
import pandas as pd
from utils import get_random_id,clear_output_folder

validemail = []         # will contain entries that pass as a valid email
invalidemail = []     # will contain entries that does not pass as a valid email
emailkey = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
phonenumbkey = "regex expression"



def emailvalidator(fname, sname, colname):
    data = pd.read_excel(fname, sname)
    df = pd.DataFrame(data)
    folder = 'emails/username/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    else:
        pass
        # clear_output_folder(folder)
    if colname in df:
        emails = df.loc[:, colname]
        for email in emails:
            checkemail = re.search(emailkey, str(email))
            if checkemail:
                matchemail = checkemail.group()
                validemail.append(matchemail)
                dname = folder+'validEmails-' + get_random_id() + '.xlsx'
                writer = pd.ExcelWriter(dname, engine='xlsxwriter')
                dataframe = pd.DataFrame(validemail, columns=["Valid Emails"])
                dataframe.to_excel(writer, sheet_name=sname, index=False)
                writer.save()
            else:
                invalidemail.append(email)
                dname = folder+'invalidEmails-' + get_random_id() + '.xlsx'
                writer = pd.ExcelWriter(dname,  engine='xlsxwriter')
                dataframe = pd.DataFrame(invalidemail, columns=["Invalid Emails"])
                dataframe.to_excel(writer, sheet_name=sname, index=False)
                writer.save()
        return dname
    else:
        return "Column name does not exist"


#def phonenumbvalidator():
 #   print "phone number validation code"

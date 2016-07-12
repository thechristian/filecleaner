import re
import pandas as pd

validemail = []         # will contain entries that pass as a valid email
invalidemailcol = []     # will contain entries that does not pass as a valid email
emailkey = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
phonenumbkey = "regex expression"


def emailvalidator(x, y):
    i = 0
    filename = str(x)
    emailcolname = str(y)
    data = pd.read_csv(filename, index_col=False)
    # check if the column name exist
    if emailcolname in data:
        emails = data.loc[:, emailcolname]
        for email in emails:
            checkemail = re.search(emailkey, email)
            if checkemail:
                matchemail = checkemail.group()
                validemail.append(matchemail)
                emailfile = open('emails/validemails.csv', 'w')  # create a file to contain valid emails
                dataframe = pd.DataFrame(validemail, columns=["Valid Emails"])
                dataframe.to_csv(emailfile, index=False)
                # emailfile.write(''.join(validemail))  # save to the file
            else:
                i =i+ 1
                index = str(i)
                invalidemailcol.append(index)
                invalidemailfile = open('emails/emailcolnum.csv', 'w')  # create a file to contain invalid emails col numbs
                dataframe = pd.DataFrame(invalidemailcol, columns=["Invalid Email Column Numbers"])
                dataframe.to_csv(invalidemailfile, index=False)
                # invalidemailfile.write(''.join(invalidemailcol))
    else:
        return "Column name does not exist"


def phonenumbvalidator():
    print "phone number validation code"

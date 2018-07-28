import os
import hashlib
from flask import Flask, render_template, request, redirect, url_for

messsage1 = hashlib.sha256()   # calling hash function to use
messsage2 = hashlib.sha256()


def checkFile(file1, file2, userfolder):
    folder = os.path.join(userfolder,'')
    openfile1 = open(file1, mode='r')  # opening file in read mode
    openfile2 = open(file2, mode='r')
    content1 = openfile1.read()  # reading the content of the file
    content2 = openfile2.read()
    messsage1.update(content1)  # passing the content of the file to the hash function
    messsage2.update(content2)
    hashed1 = messsage1.hexdigest()  # generating the hash value of the file content
    hashed2 = messsage2.hexdigest()
    # hashfile1 = open('hashes/hashvalue1', 'w')  # creating a file to save the hash values
    # hashfile2 = open('hashes/hashvalue2', 'w')
    # hashfile1.write(hashed1)  # saving the hash values to the file
    # hashfile2.write(hashed2)
    hashstring1 = str(hashed1)
    hashstring2 = str(hashed2)
    # hashfile1.close()
    # hashfile2.close()
    return hashstring1, hashstring2

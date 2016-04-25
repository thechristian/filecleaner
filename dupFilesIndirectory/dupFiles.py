import hashlib

messsage1 = hashlib.sha256()
messsage2 = hashlib.sha256()
testfile = open("testfile.txt", mode='r')
content = testfile.read()
messsage2.update(content)
messsage1.update("testing the hash function")
hashed1 = messsage1.hexdigest()
hashed2 = messsage2.hexdigest()
print  hashed2
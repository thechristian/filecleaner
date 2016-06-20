# projects (WIP)
A simple python project to
1. check for duplicate entries in a file (csv file or an excel file).
2. compare files. 

##Installation

Before you begin you would need virtualenv installed. First make sure you dont already have it by calling
`virtualenv` in your command line. No? I cannnot go through with the complete instructions at the moment but 
here is something that might help you: [Install Virtualenv](http://stackoverflow.com/questions/4324558/whats-the-proper-way-to-install-pip-virtualenv-and-distribute-for-python)

Create a virtual env by calling `virtualenv venv` (I chose 'venv' but you can call it whatever you like) and activate it.
`source venv/bin/activate` If all goes well, you should see (venv) appended to the begininng of your cli prompt. 
Right before your name.

Next is to install all the dependencies of the application, they come bundled in the requirements.txt file. Run 
`pip install -r requirements.txt` to install them.

Afterwards, you can run the application with `python app.py`

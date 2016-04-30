from dupEntries import checkForDuplicate
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 #upload file size allowed 3MB

ALLOWED_EXTENSIONS = set(['csv','txt '])    #file extensions allowed


#checking for appropriate file extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route("/")
def main():
    return render_template('index.html')	#web interface - form

@app.route('/upload', methods=['GET', 'POST'])	#getting all methods from the form
def upload_file():
    if request.method == 'POST': 	#checking if its a post method
        f = request.files['dataFile'] 	#get file name from web interface
        if f and allowed_file(f.filename):
            filepath = os.path.join('uploaded', 'uploadedNewfile')	# file saving destination and a file name
            f.save(filepath) # save file to destination
            checkForDuplicate(filepath)
        else:
            return "Error! Check file extension and upload again."
    return render_template('done.html')

if __name__ == "__main__":
    app.debug = True
    app.run()

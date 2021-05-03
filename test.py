from flask import *
from module import *
import os
import time

app = Flask(__name__)


image_name = 'profilowe.jpg'


app = Flask(__name__)
app.secret_key = "hello"


@app.route('/',)
def main():
    return render_template("index.html")




@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "POST": 
        global image_name
        isthisFile=request.files.get('file')
        print(isthisFile)
        isthisFile.save("uploads/"+isthisFile.filename)
        image_name = isthisFile.filename
        return render_template("index.html")
 
    else: 
        print('test2')
        return render_template("index.html")

@app.route('/download/<name>', methods=["POST", "GET"])
def download(name):
    
    path = f"cv/{name}.pdf"
    return send_file(path, as_attachment=True)
    

@app.route('/send', methods=["POST", "GET"])
def send():
    if request.method == "POST": 
        
        jsonData = request.get_json()
        
        wynik = sort_data(jsonData)
        print (wynik)
        print(image_name)

        path = create_cv_pdf(wynik, image_name)
        print(path)
        return render_template("index.html", path=path)
    else: 
        print('test2')
        return render_template("index.html")


    



if __name__ == "__main__":
        app.run(debug=True)
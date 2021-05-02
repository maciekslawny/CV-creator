from flask import *
from module import *


app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def main():    
    return render_template("index.html")


@app.route('/send', methods=["POST", "GET"])
def send():
    if request.method == "POST": 
        jsonData = request.get_json()
        wynik = sort_data(jsonData)
        print (wynik)
        create_cv_pdf(wynik)
        for company in wynik['experiences']:
            print(wynik['experiences'][company])
        
    
        
        return render_template("index.html")
    else: 
        print('test2')
        return render_template("index.html")






if __name__ == "__main__":
        app.run(debug=True)
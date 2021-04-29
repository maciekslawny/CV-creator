from flask import *


app = Flask(__name__)
app.secret_key = "hello"

@app.route('/')
def main():    
    return render_template("index.html")


@app.route('/send', methods=["POST", "GET"])
def send():
    if request.method == "POST": 
        jsonData = request.get_json()
        print (jsonData)
        
    
        
        return render_template("index.html")
    else: 
        print('test2')
        return render_template("index.html")






if __name__ == "__main__":
        app.run(debug=True)
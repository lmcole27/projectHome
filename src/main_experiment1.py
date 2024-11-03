from flask import Flask, render_template
import requests 

#CREATE WEBAPP
app = Flask(__name__)

#WEB HOME PAGE
@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template("index.html")

@app.route('/flask_jokes', methods=['GET', 'POST'])
def flask_jokes():
    response = requests.get('https://icanhazdadjoke.com', headers={"Accept":"application/json"})
    response.raise_for_status()
    data = response.json()
    result = data["joke"]
    print(result)
    return render_template("flask_jokes.html", result=result)

@app.route('/js_jokes', methods=['GET', 'POST'])
def js_jokes():
    return render_template("js_jokes.html")


#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
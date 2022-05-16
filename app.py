from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    if request.form['pswd'] == "poopersnooper":
        return render_template('stream.html')
    else:
        return "frig off"

# fart
if __name__ == "__main__":
    app.run(debug=True)
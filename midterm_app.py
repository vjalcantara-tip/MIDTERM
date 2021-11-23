from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('login'))
    return render_template("login.html")

@app.route('/home',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template("home.html")
    
@app.route('/registration',methods=['POST'])
def registration():
    return render_template("reg.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def main():
    return "OKKKK"

if (__name__=="__main__"):
    app.run()
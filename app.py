from flask import Flask

app=Flask(__name__)

@app.route("/home")
def home():
    return "Yo Guys.This is my homepage"
@app.route("/contactus")
def contactus():
    return "Phone Number :123456789"
@app.route("/error")
contactus()

if(__name__=="__main__"):
    app.run()
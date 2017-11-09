'''
Irene Lam
SoftDev pd7
K#13: A RESTful Journey Skyward
2017-11-10
'''
from flask import Flask, render_template
import urllib2, json
app = Flask (__name__)

@app.route("/")
def hello_world():
    data = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=PFlG6OFpBTAvtvWaeKFaRyh9keK3FRezj9cQyug2")
    url = data.geturl()
    head = data.info()
    content = data.read()
    d = json.loads()
    return render_template("nasa.html", head = head, content = content, d = url)

if __name__ == "__main__":
    app.debug = True
    app.run()

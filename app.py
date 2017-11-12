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
    try:
        data = urllib2.urlopen("http://api.mywot.com/0.4/public_link_json2?hosts=google.com/&callback=process&key=d0cc56daa6619b889f626ef9f0766eff582df53b")
        datam = data.read()[8:-1]
        d = json.loads(datam)
        print("json ->", d)
        return render_template("wot.html", level=d[d.keys()[0]]['categories'], content=d[d.keys()[0]]['target'])
    except urllib2.URLError as e:
        print e.message
        print "something went wrong"
    # url = data.geturl()
    # print url
    # head = data.info()
    # print head
    return render_template("nasa.html")


if __name__ == "__main__":
    app.debug = True
    app.run()

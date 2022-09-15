# from flask import Flask

# app = Flask(__name__)
 
# @app.route("/")
# def hello_world():
#    return "<p>Hello, World!1</p>"
 
# if __name__ == '__main__':
#    app.run(debug=True,port = 9000)

from socket import fromfd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template ("index.html")



@app.route("/searchproperty")
def searchproperty():
    search = request.args.get('search')
   #  result = cur.execute(f"SELECT * FROM books WHERE book LIKE '%{search}%'; ").fetchall()
    return  render_template("searchproperty.html")

if __name__ == '__main__':
   app.run(debug=True, port=9000)
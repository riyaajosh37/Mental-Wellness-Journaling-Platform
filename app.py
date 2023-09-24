from flask import Flask,request,Request,redirect,render_template

 
from pymongo import MongoClient

client = MongoClient('localhost',27017)
db = client.facereg
user = db.users

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")

@app.route("/register")
def reg():
    return render_template("register.html")


@app.route("/login",methods=["POST"])
def login():
    # data=request.form.to_dict()
    # fuser = user.find_one(data)
    # fid = str(fuser["_id"])
    # name = str(fuser["name"])
    # points = str(fuser["points"])
    return render_template("dashboard.html",name="Vijay",points="10")



@app.route("/startjournel")
def journel():
    return render_template("journel.html")



@app.route("/create",methods=["POST"])
def create():
    data = request.form.to_dict()
    print(data)

    # cuser = user.insert_one(data)

    return render_template("login.html")



@app.route("/task",methods=["POST"])
def task():
    data = request.form.to_dict()
    text = data["journel"]
    # tokens = nlp(text)
    # for t in tokens:
    #     if t.pos_ == 'VERB':
    #         print(t)

    task = "Sleep well for 2 Hours."
    return render_template("task.html",task = task)

@app.route("/success",methods=["POST"])
def sucess():
    return redirect("/")



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
from db import *
from flask import *


app=Flask(__name__)
app.secret_key='secretkey'


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reg")
def register():
    return render_template("register.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/ju")
def just():
    print(session.keys())
    if 'email' in session:
        flash("Login Successfull","success")
        return render_template("just.html")
    else:
        flash("Invalid login id","danger")
        return redirect('/reg')

@app.route("/fo")
def form():
    return render_template("form.html")

@app.route("/ad")
def add():
    return render_template("adminpath.html")

@app.route("/ticketpath")
def ticket():
    return render_template("ticketpath.html")

@app.route("/insert",methods=["post"])
def ins():
    name=request.form["name"]
    phone=request.form["phone"]
    email=request.form["email"]
    password=request.form["password"]
    t=(name,email,phone,password)
    insert(t)
    return redirect("/")

@app.route("/contactt",methods=["post"])
def cont():
    name=request.form["name"]
    email=request.form["email"]
    phone=request.form["phone"]
    message=request.form["message"]
    a=(name,email,phone,message)
    sendcontact(a)
    flash("Sent Successfully","success")
    return redirect("/contact")


@app.route("/reserve",methods=["post"])
def reservation():
    startfrom=request.form["startfrom"]
    destination=request.form["destination"]
    departure_date=request.form["departure date"]
    departure_time=request.form["departure time"]
    airline=request.form["airline"]
    seating=request.form["seating"]
    adult=request.form["adult"]
    children=request.form["children"]
    infant=request.form["infant"]
    trip=request.form["trip"]
    return_date=request.form["return date"]
    return_time=request.form["return time"]
    msg=request.form["msg"]
    full_name=request.form["full name"]
    phone=request.form["phone"]
    email=request.form["email"]
    r=(startfrom,destination,departure_date,departure_time,airline,seating,adult,children,infant,trip,return_date,return_time,msg,full_name,phone,email)
    print(r)
    reserve(r)
    flash("Form Submitted","successs")
    return redirect("/")

@app.route("/check",methods=["post"])
def log():
    email=request.form["email"]
    password=request.form["password"]
    t=(email,password)
    t1=select(email)
    if t in t1:
        session['email'] = email
        flash("Login Successfull","success")
        return redirect("/ju")
    else:
        flash("Invalid Userlogin","danger")
        return redirect("/reg")

@app.route("/lout")
def logout():
    print(session)
    session.clear()
    flash("Logout Successfull","primary")
    return redirect('/')

@app.route("/details")
def details():
    data=user_details()
    return render_template("details.html",a=data)


@app.route("/try",methods=["post"])
def tryit():
    email=request.form["email"]
    password=request.form["password"]
    if email=="ladaniket@gmail.com" and password=="aniket123":
        flash("Admin Login successfull","success")
        return redirect("/details")
    flash("Admin Login unsuccessfull","danger")
    return redirect("/")

@app.route("/reserved",methods=["post"])
def reserved():
    email=request.form['email']
    data=take(email)
    return render_template("departureticket.html",a=data)

@app.route("/return",methods=["post"])
def returning():
    email=request.form['email']
    data=take(email)
    return render_template("returnticket.html",a=data)


if __name__=="__main__":
    app.run(debug=True)
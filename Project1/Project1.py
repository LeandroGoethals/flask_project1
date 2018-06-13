from flask import Flask,render_template,request,make_response,session,flash,abort,redirect
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
mysql = MySQL(app)
#mysql config
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_DB"] = "project1"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"



def get_data(sql,params=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute(sql,params)
    except Exception as e:
        print(e)
        return False

    results = cursor.fetchall()
    db_data = []
    for row in results:
        db_data.append(list(row))
    print(db_data)

    cursor.close()
    conn.close()
    return db_data


@app.route("/data/<tabelnaam>")
def data(tabelnaam):
    data2 = get_data("SELECT * FROM " + tabelnaam)
    print(data2)
    return render_template("data.html", data=data2)


@app.route("/")
def index():
    # data = get_data("SELECT * FROM tblwielrenner WHERE ploegID = %s AND naam = %s",("102","Gilbert"))
    data = get_data("SELECT *")
    return render_template("home.html")


# @app.route("/login",methods=["GET","POST"])
# def login():
#     if request.method == "POST":
#         login = request.form.m["login"]
#         print(login)
#         return render_template("login.html")
#     else:
#         return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return index()

if __name__ == "__main__":
    app.run(debug=True)

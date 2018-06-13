from flask import Flask
from flask import Markup

from flask import Flask,render_template,request,make_response,session,flash,abort,redirect
# from flask.ext.mysql import MySQL
import os

from flask.ext.mysql import MySQL

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

@app.route("/")
def chart():
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [5, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001)
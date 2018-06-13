from flask import Flask, redirect, url_for, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)

#mysql config
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_DB"] = "faillisement"
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"


def get_data(sql, params=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    print("getting data")
    try:
        print(sql)
        cursor.execute(sql, params)
    except Exception as e:
        print(e)
        return False

    result = cursor.fetchall()
    data = []
    for row in result:
        data.append(list(row))
    cursor.close()
    conn.close()

    return data


def set_data(sql, params=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    print("Setting Data")
    # try:
    print(sql)
    cursor.execute(sql, params)
    conn.commit()
    # except Exception as e:
    # print(e)
    # return False

    # result = cursor.fetchall()
    # data = []
    # for row in result:
    # data.append(list(row))
    data = "Done"
    cursor.close()
    conn.close()

    return data

@app.route("/data")
def data():
    data2 = get_data("SELECT * FROM data")
    columnnames = get_data("SHOW columns from data")
    print(data2)
    return render_template("data.html", data=data2)
#def optimize_list(lijst):
    #new_lijst = []
@app.route("/chart")
def chart():
    data = []
    jaren = (2011, 2012, 2013)
    for jaar in jaren:
        sql = "select jaar,maand,sum(Aantal_werknemers) from data"
        sql += " where jaar = 2011 group by jaar, maand order by jaar, maand asc"
        data = get_data(sql,jaar)
    print(data)

    labels =get_data("select distinct maand from faillisement.data")
    titel ='aantal werknemers in faillisement'
    colors=['#44c8f5','pink','blue','orange']
    jaren = get_data("select distinct jaar from data")
    return render_template('chart.html',values=data, labels=labels,legend=titel, jaren=jaren)

@app.route("/")
def index():
    data = get_data("SELECT * FROM data")
    print(data)
    return render_template("template.html")


if __name__ == "__main__":
    app.run(debug=True)

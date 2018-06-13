from flask import Flask,render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL(app)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'examenDP2018'
app.config['MYSQL_DATABASE_PASSWORD'] = 'examenDP2018'
app.config['MYSQL_DATABASE_DB'] = 'zonnestelsel'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


def get_data(sql, params=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    records = []

    try:
        print(sql)
        cursor.execute(sql, params)
        result = cursor.fetchall()
        for row in result:
            records.append(list(row))

    except Exception as e:
        print("Fout bij het ophalen van data: {0})".format(e))

    cursor.close()
    conn.close()
    return records


def set_data(sql, params=None):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        print(sql)
        cursor.execute(sql, params)
        conn.commit()
        print("SQL uitgevoerd")

    except Exception as e:
        print("Fout bij uitvoeren van sql: {0})".format(e))
        return False

    cursor.close()
    conn.close()

    return True


@app.route("/")
def index():
    data = get_data("SELECT * FROM planeten")
    columnnames = get_data("SHOW columns from planeten")
    print(data)
    return render_template("index.html", data=data,comumnnames = columnnames)

@app.route("/planeet")
def planeet(plan):
    plan = str(plan)
    dataplaneet = get_data("SELECT * from planeten WHERE naam == (%s)" (plan) )

    return render_template("planeet.html", dat = dataplaneet)


if __name__ == "__main__":
    app.run(debug=True)

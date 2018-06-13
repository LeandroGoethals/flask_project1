from flask import Flask, render_template
from flaskext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL(app)
#mysql config
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_DB"] = "webshop"
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

@app.route('/')
def index():
    data = get_data("SELECT *")
    return render_template("index.html")
@app.route("/cookies")
def cookies():
    from flask import make_response, request

    if request.cookies.get('aantalbezoeken'):
        aantalbezoeken = str(int(request.cookies.get('aantalbezoeken')) + 1)
    else:
        aantalbezoeken = "1"
    response = make_response(render_template("cookies.html"))

    response.set_cookie("aantalbezoeken",aantalbezoeken )

    return response
@app.route("/products",methods=['POST','GET'])
def products():
    list_products = ""



if __name__ == '__main__':
    app.run(debug=True)

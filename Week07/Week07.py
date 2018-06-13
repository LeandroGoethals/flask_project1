from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    # haal de afbeeldingen op
    import os
    list_afbeeldingen = os.listdir(os.path.dirname(os.path.abspath(__file__))+'/static/images')
    # haal de productinfo op uit de tekstfile
    list_products = lees_producten('products.txt')
    return render_template('products.html', images=list_afbeeldingen, products=list_products)


@app.route('/productOverview/<productname>')
def product_overview(productname):
    list_products = lees_producten('products.txt')

    result = ""

    for product in list_products:
        if product[0] == productname:
            result = product

    if result=="":
        return render_template('dummy.html', tekst='product niet gevonden')
    else:
        return render_template('productOverview.html', product=result)



@app.route('/contact')
def contact():
    return render_template('dummy.html')


@app.route('/about')
def about():
    return render_template('about.html')


# errorhandlers
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def internal_error(error):
    return render_template('505.html', error=error)


def lees_producten(bestand):
    import os
    bestandsnaam = os.path.dirname(os.path.abspath(__file__)) + "/static/" + bestand
    list_products = []
    try:
        fp = open(bestandsnaam, 'r')
    except FileNotFoundError:
        print("File not Found!")
        return False
    lijn = fp.readline()
    while lijn != "":
        list_lijn = lijn.split(":")
        list_products.append(list_lijn)
        lijn = fp.readline()
    fp.close()
    return list_products


if __name__ == '__main__':
    app.run(debug=True)

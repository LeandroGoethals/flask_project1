# importeer de flask library
from flask import Flask

# Maak een applicatie-object aan
app = Flask(__name__)
def header(titel):
    hdr = '<!doctype html><html lang="en">'
    hdr += '<head><meta charset="UTF-8"><meta name="viewport"content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge"><link rel="stylesheet" href="http://127.0.0.1:5000/static/css/style.css"><title>Document</title></head><body><h1>NMCT</h1><table><tr><td>naam</td><td>groep</td></tr><tr><td>Leandro Goethals</td><td>1NMCT6</td></tr></table></body></html>'
    return hdr

# oefening 1
@app.route('/showinfo/<naam>/<groep>')
def show_info(naam, groep):
    if groep.upper().find("NMCT4") and groep.upper().find("NMCT6"):
        from flask import redirect
        return redirect("/error",404)
    else:
        html = header("oefening 2")
        html = '<body><h1>NMCT</h1><table><tr><td>naam</td><td>groep</td></tr>'
        html += '<tr><td>{0}</td><td>{1}</td></tr>'.format(naam, groep)
        html += '</table></body></html>'
        return html
#error
@app.route("/error")
def error():
    html = header("ERROR!")
    html += '<body>U koos de foute groep</body></html>'
    return html
@app.route('/tooninfo')
def toon_info():
    scores = get_scores()
    if scores:
        html = header("oefening 3: scores")
        html += '<body><table></body>'
        html += '<tr><th>Student</tr></th>'
        for i in range(len(scores[0])-1):
            html +='<th>Module'+ str(i+1)+'</th>'
        html += '</tr>'
        #overlopen a elke student
        for student in scores:
            html +='<tr>'
            #overlopen van alle gegevens van één student
            for gegeven in student:
                html += '<td>'+gegeven + '</td>'
            html += '</tr>'
        html += '</table>'
    else:
        html = "<body><p> File kon niet worden gevonden </p>"
    html += '</html>'
    return html
def get_scores():
    import os
    scores = []
    bestand = os.path.dirname(os.path.abspath(__file__)) + "/Scores.txt"
    try:
        fp = open(bestand, 'r')
    except FileNotFoundError:
        print("File not found!")
        return False
    lijn = fp.readline()
    while lijn != "":
        list_lijn = lijn.split(":")
        scores.append(list_lijn)
        lijn = fp.readline()
    return scores
@app.route('/priemgetallen/<mini>/<maxi>')
def priemgetallen(mini,maxi):
    if mini > maxi:
        mini,maxi = maxi,mini
    html = header("oef4:priemgetallen")
    html += "<h1> Priemgetallen van" + mini + " tot " + maxi + "</h1>"
    html += "<ul>"
    for getal in range(int(mini), int(maxi)):
        if getal > 1:
            for i in range(2,getal):
                if getal % i == 0:
                    break
                else:
                    html += "<li>"+str(getal)+"</li>"
                    break
        html += "</ul>"

    return min
    # start de Flask server met debug
@app.route('/toonkalendervandaag')
def toonkalendervandaag():
    import datetime

    return bouwkalender(datetime.date.today())
def bouwkalender(datum):
    import calendar
    jaar = datum.year
    maand = datum.month
    dag = datum.day
    html = header("oefening5: kalender van " + datum.strftime("%B"))
    html += '<body><h1>'+datum.strftime("%B")+'</h1></body>'
    html += '<table><tr><th>Maandag</th><th>Dinsdag</th><th>Woensdag</th><th>Donderdag</th><th>Vrijdag</th><th>Zaterdag</th><th>Zondag</th></tr>'

    cal = calendar.Calendar()
    calmonth = cal.monthdatescalendar(jaar, maand)
    for calweek in calmonth:
        html += '<tr>'
        for calday in calweek:
            if calday.month == maand:
                if calday.day == dag:
                    html += '<td class="today">'+str(calday.day) + '</td>'
                else:
                    html += '<td>' + str(calday.day) + '</td>'
            else:
                html += '<td>&nbsp;</td>'
        html += '</tr>'
    html += '</table>'
    return html
if __name__ == '__main__':
    app.run(debug=True)

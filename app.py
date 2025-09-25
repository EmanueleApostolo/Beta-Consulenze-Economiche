from flask import Flask, request, url_for, redirect, render_template

app=Flask(__name__)


#Home page in italiano e in inglese
@app.route('/')
def home_ita():
    return render_template('home_ita.html')
@app.route('/eng')
def home_eng():
    return render_template('index_eng.html')

#Pagine dei contatti in italiano e in inglese
@app.route('/contatti')
def contatti_ita():
    return render_template('contatti_ita.html')


#Pagine attività in italiano
@app.route('/ass_agcm')
def ass_agcm_ita():
    return render_template('ass_agcm_ita.html')
@app.route('/danni')
def danni_ita():
    return render_template('danni_ita.html')
@app.route('/energia')
def energia_ita():
    return render_template('energia_ita.html')
@app.route('/regolatorio')
def regolatorio_ita():
    return render_template('regolatorio_ita.html')
@app.route('/aiuti_stato')
def aiuti_stato_ita():
    return render_template('aiuti_stato_ita.html')
@app.route('/arbitrati')
def arbitrati_ita():
    return render_template('arbitrati_ita.html')



if __name__ == "__main__":
    app.run()

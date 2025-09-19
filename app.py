from flask import Flask, request, url_for, redirect, render_template

app=Flask(__name__)

@app.route('/card')
def card():
    return render_template('prova.html')

@app.route('/home')
def index():
    return render_template('CE_home.html')

@app.route('/home_eng')
def index_eng():
    return render_template('CE_home_eng.html')

@app.route('/contatti')
def contatti():
    return render_template('contatti.html')

@app.route('/contatti_eng')
def contatti_eng():
    return render_template('contatti_eng.html')

#@app.route('/team_as')
#def team_as():
    #return render_template('alessia.html')

#@app.route('/team_cs')
#def team_cs():
    #return render_template('carlo.html')

@app.route('/sostegnoagcm')
def sostegnoagcm():
    return render_template('sostegnoagcm.html')

@app.route('/sostegnoagcm_eng')
def sostegnoagcm_eng():
    return render_template('sostegnoagcm_eng.html')

@app.route('/quantificazionedanni')
def quantificazionedanni():
    return render_template('quantificazionedanni.html')

@app.route('/quantificazionedanni_eng')
def quantificazionedanni_eng():
    return render_template('quantificazionedanni_eng.html')

@app.route('/mercatienergia')
def mercatienergia():
    return render_template('mercatienergia.html')

@app.route('/mercatienergia_eng')
def mercatienergia_eng():
    return render_template('mercatienergia_eng.html')

@app.route('/assistenzaoperazioni')
def assistenzaoperazioni():
    return render_template('assistenzaoperazioni.html')

@app.route('/assistenzaoperazioni_eng')
def assistenzaoperazioni_eng():
    return render_template('assistenzaoperazioni_eng.html')

@app.route('/consulenzaregolatoria')
def consulenzaregolatoria():
    return render_template('consulenzaregolatoria.html')

@app.route('/consulenzaregolatoria_eng')
def consulenzaregolatoria_eng():
    return render_template('consulenzaregolatoria_eng.html')

@app.route('/aiutidistato')
def aiutidistato():
    return render_template('aiutidistato.html')

@app.route('/aiutidistato_eng')
def aiutidistato_eng():
    return render_template('aiutidistato_eng.html')

@app.route('/arbitrati')
def arbitrati():
    return render_template('arbitrati.html')

@app.route('/arbitrati_eng')
def arbitrati_eng():
    return render_template('arbitrati_eng.html')

@app.route('/pubblicazioniaiutidistato')
def pubblicazioniaiutidistato():
    return render_template('pubblicazioniaiutidistato.html')

@app.route('/pubblicazioniaiutidistato_eng')
def pubblicazioniaiutidistato_eng():
    return render_template('pubblicazioniaiutidistato_eng.html')

@app.route('/pubblicazioniprocessicompetitivi')
def pubblicazioniprocessicompetitivi():
    return render_template('pubblicazioniprocessicompetitivi.html')

@app.route('/pubblicazioniprocessicompetitivi_eng')
def pubblicazioniprocessicompetitivi_eng():
    return render_template('pubblicazioniprocessicompetitivi_eng.html')

@app.route('/pubblicazioniteoriaregolazione')
def pubblicazioniteoriaregolazione():
    return render_template('pubblicazioniteoriaregolazione.html')

@app.route('/pubblicazioniteoriaregolazione_eng')
def pubblicazioniteoriaregolazione_eng():
    return render_template('pubblicazioniteoriaregolazione_eng.html')

@app.route('/pubblicazioniservizipubblici')
def pubblicazioniservizipubblici():
    return render_template('pubblicazioniservizipubblici.html')

@app.route('/pubblicazioniservizipubblici_eng')
def pubblicazioniservizipubblici_eng():
    return render_template('pubblicazioniservizipubblici_eng.html')

@app.route('/pubblicazionifinanzainfrastrutture')
def pubblicazionifinanzainfrastrutture():
    return render_template('pubblicazionifinanzainfrastrutture.html')

@app.route('/pubblicazionifinanzainfrastrutture_eng')
def pubblicazionifinanzainfrastrutture_eng():
    return render_template('pubblicazionifinanzainfrastrutture_eng.html')

@app.route('/pubblicazionimercatienergia')
def pubblicazionimercatienergia():
    return render_template('pubblicazionimercatienergia.html')

@app.route('/pubblicazionimercatienergia_eng')
def pubblicazionimercatienergia_eng():
    return render_template('pubblicazionimercatienergia_eng.html')

if __name__ == "__main__":
    app.run()




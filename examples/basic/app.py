from pyweb.pyweb import Pyweb

app = Pyweb()

@app.route('/', 'GET')
def index():
    return { 'test': '123' }

app.run(debug=True)
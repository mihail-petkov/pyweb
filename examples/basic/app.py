from pyweb.pyweb import Pyweb

app = Pyweb()

@app.route('/', 'GET')
def index():
    return { 'test': '123' }

@app.route('/test', 'GET')
def index():
    return { 'test': '123' }

@app.route('/test', 'POST')
def index():
    return { 'test': '123' }

@app.route('/test/<deviceId>/device', 'POST')
def index():
    return { 'test': '123' }

@app.route('/test/<deviceIds>/device/', 'GET')
def index():
    return { 'test': '123' }

app.run(debug=True)
from pyweb.pyweb import Pyweb
import pyweb.ctx as ctx

app = Pyweb()

@app.route('/', 'GET')
def index():
    return { "test": "123" }

@app.route('/test', 'GET')
def index():
    return { "test": "GET response" }, 201, { "Content-Type": 'application/json', "Authentication": '123'}

@app.route('/test', 'POST')
def index():
    return { "test": "POST response" }

@app.route('/test/<deviceId>/device', 'POST')
def index():
    return { "test": "123" }

@app.route('/test/<deviceId>/device/<testId>/run', 'POST')
def index(device_id, test_id):
    print(device_id)
    print(test_id)
    print(ctx.request.path)
    print(ctx.request.type)
    print(ctx.request.body)
    print(ctx.request.params)
    return { "test": "123" }

app.run(debug=True)
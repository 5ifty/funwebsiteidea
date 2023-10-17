from flask import Flask, render_template


sys.path.append('/')

app = Flask(__name__, template_folder='templates', static_folder='static')

@route('/', methods=['GET'])
def index(self):
    return render_template('HTML.html')

Flasky.register(app,route_base = '/')
app.logger.removeHandler(default_handler)


if __name__ == "__main__":
  app.run(debug='True', host='0.0.0.0', port=3000)
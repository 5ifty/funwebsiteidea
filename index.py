from flask import Flask, render_template
import sys

sys.path.append('/')

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET'])
def index():
    return render_template('HTML.html')

if __name__ == "__main__":
    app.run(debug=True, host='13.49.0.1', port=3000)
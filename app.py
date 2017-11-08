from flask import Flask
from jt.finances import handler

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/fetch_test')
def fetch_test():
    handler.fetch_checking_transactions()
    handler.fetch_chase_sapphire_transactions()
    return 'Everything passed!', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

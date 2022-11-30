from flask import Flask
from internal.handlers.view import view

app = Flask(__name__)
app.add_url_rule('/turn_on', 'turn_on', view.turn_on, methods="POST")



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8123, debug=True)

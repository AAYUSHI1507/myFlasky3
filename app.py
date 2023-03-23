from flask import Flask

app = Flask(__name__)
app.secret_key = b'_thuiklstrhj/'


from routes import *

if __name__ == '__main__':
    app.run(debug=True) # type: ignore
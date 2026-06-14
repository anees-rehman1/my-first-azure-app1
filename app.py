from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello From Azure! </h1> <p> I deployed this myself! </p>"

if __name__ == '__main__':
    app.run()
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello From Azureeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee! </h1> <p> I deployed this myself as a Shadowwwwwwwwwwwwwwwwwwwwwwwww! </p>"

if __name__ == '__main__':
    app.run()

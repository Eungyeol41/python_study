from flask import Flask
app = Flask(__name__)

# 데코레이터(decorator)
@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"
app.run()
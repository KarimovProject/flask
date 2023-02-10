from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello world"

@app.route('/')
def hom():
    r = request.args
    a = int(r['a'])
    b = int(r['b'])
    s = a+b
    
    return f'summa: {s}'

if __name__=='__main__':
    app.run()
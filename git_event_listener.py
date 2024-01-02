from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    print(f'request.url:{request.url}\nrequest.payload: {request.json}\n')
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3080)
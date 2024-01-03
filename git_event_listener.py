from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root():
    print(f'request.url:{request.url}\nrequest.payload: {request}\n')
    data = request.get_json()
    print(f'{type(data)}')
    print(f'{data}')
    return Response(status=201, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3080)
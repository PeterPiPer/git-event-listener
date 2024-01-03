from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def root():
    print(f'request.url:{request.url}\nrequest.payload: {request}\n')
    #return jsonify(url=request.url)
    data = request.form.to_dict()
    print(f'{type(data)}')
    for key, item in data.items():
        print(f'{type(key)}\n{key}')
        print(f'{type(item)}\n{item}')


    for key, item in request.form.items():
        print(f'{type(key)} {type(item)}')
        print(f'{key}\n\n{item}')
    return Response(status=201, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3080)
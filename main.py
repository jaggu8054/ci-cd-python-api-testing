from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def helloworld():
	if(request.method == 'GET'):
		data = {"data": "testing ci-cd "}
		return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
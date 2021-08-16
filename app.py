from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def hello():
    return 'Hello, world'

if __name__ == "__main__":
    app.run()


from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import jsonify

app = FlaskAPI(__name__)

@app.route('/test', methods=['GET'])
def get():
        return jsonify({'headers': str(request.headers)}), 200

if __name__ == "__main__":
    app.run()

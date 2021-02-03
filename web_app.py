from songogram import send_songogram
from flask import Flask, request, send_from_directory, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('', 'index.html')


@app.route('/API/1.0.0/songogram', methods=['GET'])
def songogram():
    for item in request.args.values():
        if item == "":
            return jsonify({'status': 422,'error': 'Unprocessable Entity', 'message': 'Missing Input'})
    send_songogram(request.args.get('name'), request.args.get('artist_fname'), request.args.get('artist_lname'),
                   request.args.get('song_name'), request.args.get('number'))
    return send_from_directory('', 'success.html')


if __name__ == "__main__":
    app.run()

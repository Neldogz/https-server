from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)
key_value_store = {}
uploaded_files = {}

@app.route('/')
def index():
    return 'Welcome to to my Flask web server'

@app.route('/key-value', methods=['POST'])
def key_value():
    action = request.json.get('action')
    key = request.json.get('key')
    value = request.json.get('value')

    if action == 'set':
        key_value_store[key] = value
        return jsonify({'status': 'success'})
    elif action == 'get':
        if key in key_value_store:
            return jsonify({'status': 'success', 'value': key_value_store[key]})
        else:
            return jsonify({'status': 'error', 'message': 'Key not found'})
    elif action == 'get_all':
        return jsonify({'status': 'success', 'data': key_value_store})
    elif action == 'delete':
        if key in key_value_store:
            key_value_store.pop(key)
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'error', 'message': 'Key not found'})
    elif action == 'clear':
        key_value_store.clear()
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid action'})


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'status': 'error', 'message': 'File not found in request'}), 400

    file.save(file.filename)
    return jsonify({'status': 'success'})


@app.route('/files')
def files():
    return jsonify(uploaded_files)

@app.route('/download/<path:filename>')
def download(filename):
    if filename not in uploaded_files:
        return jsonify({'status': 'error', 'message': 'File not found'}), 404
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=False)

from flask import Flask, request, jsonify
from . import get_partition_count

app = Flask(__name__)

@app.route('/handle-intent', methods=['POST'])
def handle_intent():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    intent = data.get('intent')
    params = data.get('params')

    if intent == 'getPartitionCount':
        result = get_partition_count(params)
        return jsonify(result), 200

    return jsonify({"error": "Unsupported intent"}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from kafka_client  import get_broker_data, create_topic, read_topic_data, read_partition_data, delete_topic

app = Flask(__name__)

@app.route('/handle-intent', methods=['POST'])
def handle_intent():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    intent = data.get('intent')
    params = data.get('params')

    if intent == 'getBrokerData':
        result = get_broker_data(params)
    elif intent == 'createTopic':
        result = create_topic(params)
    elif intent == 'readTopicData':
        result = read_topic_data(params)
    elif intent == 'readPartitionData':
        result = read_partition_data(params)
    elif intent == 'deleteTopic':
        result = delete_topic(params)
    else:
        return jsonify({"error": "Unsupported intent"}), 400

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
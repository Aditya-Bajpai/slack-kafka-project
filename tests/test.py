import requests
import json

url = 'http://localhost:5000/handle-intent'

headers = {
    'Content-Type': 'application/json'
}

def run_test(name, payload):
    print(f"\n=== {name} ===")
    res = requests.post(url, headers=headers, data=json.dumps(payload))
    print("Status Code:", res.status_code)
    try:
        print("Response:", res.json())
    except Exception as e:
        print("Error decoding JSON:", e)

# 1. Get Broker Data
run_test("Test 1: getBrokerData", {
    "intent": "getBrokerData",
    "params": {
        "nodeName": "REMOTE_KAFKA",
        "clusterName": "cluster.5",
        "brokerName": "1"
    }
})

# 2. Create Topic
run_test("Test 2: createTopic", {
    "intent": "createTopic",
    "params": {
        "nodeName": "REMOTE_KAFKA",
        "clusterName": "cluster.5",
        "topicName": "cluster.4.TOPIC.651",
        "body": {
            "partitions": 3,
            "replicationFactor": 1
        }
    }
})


# 3. Read Topic Data
run_test("Test 3: readTopicData", {
    "intent": "readTopicData",
    "params": {
        "nodeName": "REMOTE_KAFKA",
        "clusterName": "cluster.5",
        "topicName": "cluster.4.TOPIC.670"
    }
})


# 4. Read Partition Data
run_test("Test 4: readPartitionData", {
    "intent": "readPartitionData",
    "params": {
        "nodeName": "REMOTE_KAFKA",
        "clusterName": "cluster.5",
        "partitionName": "cluster.4.TOPIC.670-0"
    }
})


# 5. Delete Topic
run_test("Test 5: deleteTopic", {
    "intent": "deleteTopic",
    "params": {
        "nodeName": "REMOTE_KAFKA",
        "clusterName": "cluster.5",
        "topicName": "cluster.4.TOPIC.670"
    }
})

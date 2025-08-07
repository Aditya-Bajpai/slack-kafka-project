import json
import requests

payload = {
    "intent": "getBrokerData",
    "params": {
        "nodeName": "REMOTE_KAFKA",
        "clusterName": "cluster.5",
        "brokerName": "1"
    }
}

response = requests.post("http://localhost:5000/handle-intent", json=payload)
print("Status Code:", response.status_code)
print("Response:", response.json())

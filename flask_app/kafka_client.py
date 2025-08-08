import requests


def get_broker_data(params):
    try:
        base_url = "http://129.80.133.91:8019"  # ✅ Your API server address
        url = f"{base_url}/rest/v1/kafka/brokers/{params['nodeName']}/{params['clusterName']}/{params['brokerName']}"
        res = requests.get(url, auth=('Admin', 'admin'))
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}


AUTH = ('Admin', 'admin')
BASE_URL = "http://129.80.133.91:8019/rest/v1"

def create_topic(params):
    try:
        url = f"{BASE_URL}/kafka/topics/{params['nodeName']}"
        res = requests.post(url, json=params['body'], auth=AUTH)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def read_topic_data(params):
    try:
        url = f"{BASE_URL}/kafka/topics/{params['nodeName']}/{params['clusterName']}/{params['topicName']}?attributes={params.get('attributes', '*')}"
        res = requests.get(url, auth=AUTH)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def read_partition_data(params):
    try:
        url = f"{BASE_URL}/kafka/partitions/{params['nodeName']}/{params['clusterName']}/{params['partitionName']}?attributes={params.get('attributes', '*')}"
        res = requests.get(url, auth=AUTH)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def delete_topic(params):
    try:
        url = f"{BASE_URL}/kafka/topics/{params['nodeName']}/{params['clusterName']}/{params['topicName']}"
        res = requests.delete(url, auth=AUTH)
        res.raise_for_status()
        return {"message": "Topic deleted successfully"}
    except Exception as e:
        return {"error": str(e)}

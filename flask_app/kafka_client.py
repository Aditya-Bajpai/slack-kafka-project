import requests


def get_broker_data(params):
    try:
        url = f"http://{params['nodeName']}/kafka/brokers/{params['nodeName']}/{params['clusterName']}/{params['brokerName']}"
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def create_topic(params):
    try:
        url = f"http://{params['nodeName']}/kafka/topics"
        res = requests.post(url, json=params['body'])
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def read_topic_data(params):
    try:
        url = f"http://{params['nodeName']}/kafka/topics/{params['nodeName']}/{params['clusterName']}/{params['topicName']}"
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def read_partition_data(params):
    try:
        url = f"http://{params['nodeName']}/kafka/partitions/{params['nodeName']}/{params['clusterName']}/{params['partitionName']}"
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        return {"error": str(e)}

def delete_topic(params):
    try:
        url = f"http://{params['nodeName']}/kafka/topics/{params['nodeName']}/{params['clusterName']}/{params['topicName']}"
        res = requests.delete(url)
        res.raise_for_status()
        return {"message": "Topic deleted successfully"}
    except Exception as e:
        return {"error": str(e)}

import requests

def get_partition_count(params):
    topic = params.get('topicName')
    cluster = params.get('clusterName')  # Might not be needed unless URL-specific
    node = params.get('nodeName')

    if not topic or not node:
        return {"error": "Missing topicName or nodeName"}

    url = f"http://{node}/topics/{topic}/partitions"

    try:
        response = requests.get(url)
        response.raise_for_status()
        partitions = response.json()
        return {"topic": topic, "partition_count": len(partitions)}
    except Exception as e:
        return {"error": str(e)}

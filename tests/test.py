import requests
from requests.auth import HTTPBasicAuth
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.passwords import user, password

node = "REMOTE_KAFKA"
cluster = "cluster.5"
broker = "1"

url = f"http://129.80.133.91:8019/rest/v1/kafka/brokers/{node}/{cluster}/{broker}"
auth = HTTPBasicAuth(user, password)

try:
    res = requests.get(url, auth=auth)
    print("Status:", res.status_code)
    print("Response:", res.json())
except Exception as e:
    print("Error:", e)

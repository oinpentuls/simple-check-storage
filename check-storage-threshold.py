import requests
import socket
import subprocess
import config

df = subprocess.Popen(["df", "-HPl"], stdout=subprocess.PIPE)

grep = subprocess.Popen(["grep", "^/dev"], stdin=df.stdout ,stdout=subprocess.PIPE)

getStorage = subprocess.Popen(["awk", "{print $5}"], stdin=grep.stdout, stdout=subprocess.PIPE) 

usedStorage = subprocess.run(["sed", "s/%//"], stdin=getStorage.stdout, text=True, capture_output=True).stdout

serverName = socket.gethostname()

if int(usedStorage) >= config.STORAGE_THRESHOLD:
    payload = {"ServerName": serverName, "Threshold": config.STORAGE_THRESHOLD}
    url = config.BOT_URL + "/ServerReport/StorageThreshold"
    
    result = requests.get(url, params=payload)

print(usedStorage)


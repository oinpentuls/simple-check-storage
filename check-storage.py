import requests
import socket
import subprocess
import config

df = subprocess.Popen(["df", "-HPl"], stdout=subprocess.PIPE)

grep = subprocess.Popen(["grep", "^/dev"], stdin=df.stdout ,stdout=subprocess.PIPE)

storage = subprocess.run(["awk", "{print $2, $4, $5, $6}"], stdin=grep.stdout, text=True, capture_output=True).stdout

splitStorage = storage.split()

totalSize = splitStorage[0]
freeSize = splitStorage[1]
serverName = socket.gethostname()

payload = {"ServerName": serverName, "TotalSize": totalSize, "FreeSize": freeSize}

# This url is used to send the result to log server
if config.BOT_URL:
    url = config.BOT_URL + "/ServerReport"
    result = requests.get(url, params=payload)
    print(result)


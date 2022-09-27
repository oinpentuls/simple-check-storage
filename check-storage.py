import requests
import socket
import subprocess

df = subprocess.Popen(["df", "-HPl"], stdout=subprocess.PIPE)

grep = subprocess.Popen(["grep", "^/dev"], stdin=df.stdout ,stdout=subprocess.PIPE)

storage = subprocess.run(["awk", "{print $2,$4, $5, $6}"], stdin=grep.stdout, text=True, capture_output=True).stdout

splitStorage = storage.split()

totalSize = splitStorage[0]
freeSize = splitStorage[1]
serverName = socket.gethostname()

payload = {"ServerName": serverName, "TotalSize": totalSize, "FreeSize": freeSize}

# This url is used to send the result to log server
url = ""

if url:
    result = requests.get(url, params=payload)
    print(result)


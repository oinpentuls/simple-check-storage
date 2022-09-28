# simple-check-storage

## clone this repo to your server

```
git clone https://github.com/oinpentuls/simple-check-storage.git
```

## Add config file
create file called `config.py` in the root and insert this piece of code.
```py

# actually it can whatever you want, but i'm using bot
BOT_URL="your bot url"

# Threshold for your storage, used to compare with server storage
STORAGE_THRESHOLD = 90
```

## Available script
- Check storage capacity
- Check if the storage reaching the threshold you set.

## Usage
Run this script with cron

### example
Run the storage checking 3 times every month at 10AM on 7, 14 and 28
```sh
00 10 7,14,28 * * python3 /var/home/usr/simple-check-storage/check-storage.py
```

Send alert if storage reach 90% at 9AM
```sh
00 09 * * python3 /var/home/usr/simple-check-storage/check-storage-threshold.py
```

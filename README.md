# WebHook
cpualert.py ---> Discord webhook that sends Notification if cpu and memory exceeds at certian level..!
pcusage.py ---> Discord webhook that sends Notification About Your PC Usage (cpu, mem, disk) at every 100s..!

## WARNING
Iam a beginner, My code may be junky...!   
# Installation
```bash
$ git clone https://github.com/Humanpredator/Discord-Webhooks
$ cd Discord-Webhooks
```
## CONFIG VARS
Fill the following in config.env.\
--> WEBHOOK_URL = '' #Use your discord text channel webhook URL.\
--> USERNAME = '' #Name for your webhook, leave it for default.\
--> CPU_USG_LMT = '50' #Enter Your Cpu Usage Limit, leave it for default.\
--> MEM_USG_LMT = '50' #Enter Your Ram Usage Limit, leave it for default.

## Install Requirements
```bash
$ pip install -r requirements-cli.txt
```
--> Require Python 3.7
If requirements-cli.txt didn't Work just try to install all requirement module individually...!
## RUN
```
$ python cpualert.py
```
```
$ python pcusage.py
```

##### Or --> Simply Click Run if your'e using VS Code...!

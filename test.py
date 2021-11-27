import json
with open('ibm-db2-credentials.json', 'r') as credentialsFile:
    credentials1 = json.loads(credentialsFile.read())
s = credentials1['connection']['db2']['hosts'][0]['port']
print(str(s))
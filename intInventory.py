#!/usr/bin/env python2.7
# create interface inventory
import json
import requests
#

ip = '192.168.1.15'

my_headers = {'content-type': 'application/json-rpc'}
url = "http://"+ip+"/ins"
username = "cisco"
password = "cisco"

intfDict = {}

showCmd = "show int desc"
payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": showCmd,
                     "version": 1},
          "id": 1}
         ]
response = requests.post(url, data=json.dumps(payload), 
    headers=my_headers, auth=(username, password)).json()

for element in response['result']['body']['TABLE_interface']['ROW_interface']:
    intfName = str(element['interface'])
    try:
        intfDesc = str(element['desc'])
    except:
        intfDesc = "NONE"
    intfDict[intfName] = {}
    intfDict[intfName]['desc'] = intfDesc

showCmd = "show int status"
payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": showCmd,
                     "version": 1},
          "id": 1}
         ]
response = requests.post(url, data=json.dumps(payload), 
    headers=my_headers, auth=(username, password)).json()
    
for element in response['result']['body']['TABLE_interface']['ROW_interface']:
    intfName = str(element['interface'])
    try:
        intfState = str(element['state'])
    except:
        intfState = "UNKN"
    intfDict[intfName]['state'] = intfState
 
for element in intfDict:
    print element,intfDict[element]['state'],intfDict[element]['desc']
 


        


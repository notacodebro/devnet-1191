#!/usr/bin/python3

import requests
import json 
import argparse
import getpass
import base64
import urllib3
import pandas as pd
from tabulate import tabulate


#BASE_URL = 'https://172.17.7.200'
BASE_URL = 'https://sandboxdnac.cisco.com'
POPPED_TAGS = ['scoreList', 'starttime', 'endtime', 'maintenanceAffectedClientCount', 'duidCount', 'randomMacCount']
urllib3.disable_warnings()

def authentication(material):
    url = f'{BASE_URL}/dna/system/api/v1/auth/token'
    headers = {"Content-Type":"application/json", "Accept":"application/json", "Authorization":f"Basic {material}"}
    request = requests.post(url, headers=headers, verify=False)
    return request

def get_clients(token_header):
    meta = 'client_health'
    client_health = f'{BASE_URL}/dna/intent/api/v1/client-health' 
    request = requests.get(client_health, headers=token_header, verify=False)
    return json.loads(request.text), meta
 
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='community string for snmp', required=True)
    parser.add_argument('--mac', help='community string for snmp', required=False)
    parser.add_argument('--interactive', help='community string for snmp', required=False)
    args = parser.parse_args()
    return args

def printer(results, meta):
    popped_tags = ['scoreList', 'starttime', 'endtime', 'maintenanceAffectedClientCount', 'duidCount', 'randomMacCount']
    results = results['response'][0]['scoreDetail']
    try: 
        for items in results[1]['scoreList']:
            items.pop('scoreList')
    except KeyError:
        pass
    pdresult = pd.json_normalize(results[0])
    pdresult_specific = pd.json_normalize(results[1]['scoreList'])
    for items in popped_tags:
        try:
            pdresult.pop(items)
            pdresult_specific.pop(items)
        except KeyError:
            pass
    print()
    print('Global Client Health Results')
    print('*'*64)
    print(tabulate(pdresult, headers='keys'))
    print('Specific Health Results')
    print('*'*64)
    print(tabulate(pdresult_specific, headers='keys'))

def main():
    print('*'*64)
    print('Welcome to the Catalyst Center Client Health Check Tool')
    print('*'*64)
    args = parser()
    password = getpass.getpass() 
    material = base64.b64encode(f'{args.username}:{password}'.encode())
    material = material.decode()
    token = authentication(material)
    token = token.json()['Token']
    token_header = {'X-Auth-Token': token, 'Content-Type': 'application/json'}
    if args.mac:
        results, meta = get_client(token_header, args.mac)
    else:
        print('Please wait....')
        results, meta =  get_clients(token_header)
    
    printer(results, meta)


main()
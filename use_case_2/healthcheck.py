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
    _url = f'{BASE_URL}/dna/system/api/v1/auth/token'
    _headers = {"Content-Type":"application/json", "Accept":"application/json", "Authorization":f"Basic {material}"}
    request = requests.post(_url, headers=_headers, verify=False)
    return request

def get_clients(token_header):
    meta = 'client_health'
    _url = f'{BASE_URL}/dna/intent/api/v1/client-health' 
    request = requests.get(_url, headers=token_header, verify=False)
    return json.loads(request.text), meta
 
 def get_hosts():
    pass
def parser():
    _parser = argparse.ArgumentParser()
    _parser.add_argument('--username', help='community string for snmp', required=True)
    _parser.add_argument('--mac', help='community string for snmp', required=False)
    _parser.add_argument('--interactive', help='community string for snmp', required=False)
    args = _parser.parse_args()
    return args

def printer(results, meta):
    _popped_tags = ['scoreList', 'starttime', 'endtime', 'maintenanceAffectedClientCount', 'duidCount', 'randomMacCount']
    _results = results['response'][0]['scoreDetail']
    try: 
        for items in _results[1]['scoreList']:
            items.pop('scoreList')
    except KeyError:
        pass
    _pdresult = pd.json_normalize(_results[0])
    _pdresult_specific = pd.json_normalize(_results[1]['scoreList'])
    for items in _popped_tags:
        try:
            _pdresult.pop(items)
            _pdresult_specific.pop(items)
        except KeyError:
            pass
    print()
    print('Global Client Health Results')
    print('*'*64)
    print(tabulate(_pdresult, headers='keys'))
    print('Specific Health Results')
    print('*'*64)
    print(tabulate(_pdresult_specific, headers='keys'))

def main():
    print('*'*64)
    print('Welcome to the Catalyst Center Client Health Check Tool')
    print('*'*64)
    args = parser()
    _password = getpass.getpass() 
    material = base64.b64encode(f'{args.username}:{_password}'.encode())
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
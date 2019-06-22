import requests
requests.packages.urllib3.disable_warnings()
import sys
import json
def get_token():
        bao_auth_url = "https://<bao server>/baocdp/rest/login"
        username = sys.argv[1]
        password = sys.argv[2]
        message_json = {"username": username,"password": password}
        message_headers={'Content-Type': 'application/json'}
        response = requests.post(bao_auth_url, json=message_json, headers=message_headers, verify=False)
        headers = response.headers
        token = headers['Authentication-Token']
        return(token)
def run_process(targets):
        print("executing against:",targets)
        bao_process_url = "https://<bao server>:38080/baocdp/rest/process/:Module:Process/execute"
        message_json = {"inputParameters": [{"name": "target", "value": targets}]}
        message_headers={'Authentication-Token': get_token()}
        response = requests.post(bao_process_url, json=message_json, headers=message_headers, verify=False)
        headers = response.headers
        print(response.json())
        return(response.json())
targets = sys.argv[3]
results = (run_process(targets))
print(results)

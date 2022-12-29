import subprocess
import requests
from requests.auth import HTTPDigestAuth
import json
import getpass
import traceback
from OntimDevTool import auth_server
from OntimDevTool import secure_access

def get_cpu_id():
    ret = subprocess.run(['fastboot', 'oem', 'get_device_id'], capture_output=True)
    cpu_id = ret.stderr.decode('ascii').split('\n')[0].split('(bootloader) ')[1].strip()
    return cpu_id

def auth_start():
    # step 1, get nonce by run 'fastboot oem f_auth_start'
    ret = subprocess.run(['fastboot', 'oem', 'f_auth_start'], capture_output=True)
    nonce = ret.stderr.decode('ascii').split('\n')[5].split('(bootloader) ')[1]
    print(f"Success to get nonce from the phone: {nonce} \n")
    return nonce

def sign(nonce, project):
    # step 2, get auth response from auth server
    cpuid = get_cpu_id()
    print(f"cpu_id = {cpuid}\n")

    print("Waiting for sign from anth server...")
    header = {"Content-Type": "application/json"}

    if (secure_access):
        username = input("Please input username, empty for default user: ")
        password = getpass.getpass("Please input password, empty for default password: ")
        if not username:
            username = "admin"
            password = "123456"
        auth = HTTPDigestAuth(username, password)
        ret = requests.get(auth_server + "Token/", auth = auth)
        token = json.loads(ret.content.decode('ascii'))['token']
        header["Authorization"] = "Bearer "+ token

    payload = {"project": project, "cpuid": cpuid, "nonce": nonce}
    ret = requests.post(auth_server + "AuthDownload/", headers = header, data = json.dumps(payload))
    try:
        auth_resp = json.loads(ret.content.decode('ascii'))['nonce']
        print(f"Success to get the signature: {auth_resp} \n")
    except Exception as ex:
        print(f"Failed to get the signature!!! Auth Server returns:\n{ret.content}")
        print(traceback.print_exc())
    return auth_resp

def permission(auth_resp):
    # step 3, get auth response to phone to verify, by run 'fastboot oem permission factory xxxxxx
    ret = subprocess.run(['fastboot', 'oem', 'permission', 'factory', auth_resp], capture_output=True)
    print(f"Authorise result: \n {ret.stderr.decode('ascii')}")
    return ret

def authorise(project):
    print("Please go into fastboot mode...")
    nonce = auth_start()         # step 1, get nonce by run 'fastboot oem f_auth_start'
    signed_data = sign(nonce, project)    # step 2, get auth response from auth server
    permission(signed_data)           # step 3, send auth response to phone to verify, by run 'fastboot oem permission factory xxxxxx

def edl(project):
    authorise(project)
    ret = subprocess.run(['fastboot', 'oem', 'edl'], capture_output=True)
    print(f"edl result: \n {ret.stderr.decode('ascii')}")
    return ret

def offline_auth_01_get_nonce():
    print("Please go into fastboot mode...")
    nonce = auth_start()         # step 1, get nonce by run 'fastboot oem f_auth_start'
    print(f"nonce: {nonce}")
    return nonce

def offline_auth_02_get_sign(nonce):
    signed_data = sign(nonce)
    print(f"signed_data: {signed_data}")
    return signed_data

def offline_auth_03_set_permission(signed_data):
    permission(signed_data)

if __name__ == "__main__":
    authorise("venom")

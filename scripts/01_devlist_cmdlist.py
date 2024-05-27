from scrapli import Scrapli
from scrapli.exceptions import ScrapliException
import pprint
import yaml


fq_list = []
sn_list = []

SSH_FILE = '01_secret.yml'

with open(SSH_FILE, 'r') as s:
    sfile = yaml.safe_load(s)
    rtr_user = sfile['RTR_SSH_USERNAME']
    rtr_file = sfile['RTR_SSH_CONFIG']
    wlc_user = sfile['WLC_USERNAME']
    wlc_pas = sfile['WLC_PASSWORD']    
    
DEVLIST_FILE = '01_devlist.yml'

            
def iosxe_sh_cmd():
    with open(DEVLIST_FILE, 'r') as f:
        devs = yaml.safe_load(f)
    for iosxe in devs["iosxe"]:
        print(f"\n\n**************************\nConnecting to {iosxe}\n**************************\n")
        device = {
            "host": iosxe,
            "auth_username": rtr_user,
            "auth_strict_key": False,
            "ssh_config_file": rtr_file,
            "platform": "cisco_iosxe"
        }
        try:
            conn = Scrapli(**device)
            conn.open()
            response = conn.send_command("show ver")
            sn = response.textfsm_parse_output()[0]["serial"]
            fq = response.textfsm_parse_output()[0]["hostname"]
            #FOLLOWING IS NOT NEEDED
            #pprint.pprint(response.textfsm_parse_output()[0]["serial"])
            sn_list.append(sn)
            fq_list.append(fq)
            conn.close()
        except (ScrapliException): 
            print(f"\n\nConnection to {iosxe} FAILED!")
            continue
        #auth_private_key": "/Users/USERNAME/.ssh/id_rsa",
        #response.textfsm_parse_output() is a list of one element - dictionary
        rtsw_in_use_dick = dict(zip(fq_list, sn_list))
        #Uncomment in case of debugging:
        pprint.pprint(rtsw_in_use_dick, width = 80, indent=4)
        return rtsw_in_use_dick

def main():
    iosxe_sh_cmd()


if __name__ == "__main__":
    main()
    
"""
(venv-scrapli) gandalf@debian11:~/repo_scrapli$ python3 01_devlist_cmdlist.py 


**************************
Connecting to 192.168.100.9
**************************



Connection to 192.168.100.9 FAILED!


**************************
Connecting to 192.168.100.8
**************************

{'router01': ['12345678']}

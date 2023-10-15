from ncclient import manager
import xmltodict
import pprint

device = {
    "host": "192.168.100.13",
    "username": "gandalf",
    "password": "grey",
    "port": 830,    
}


sn_sw_filter = """
<filter>
    <device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper">
        <device-hardware>
            <device-inventory>
                <hw-type>hw-type-chassis</hw-type>
            </device-inventory>
            <device-system-data></device-system-data>
        </device-hardware>
    </device-hardware-data>
</filter>
"""

with manager.connect(**device, hostkey_verify=False) as m:
    ncclient_response = m.get(sn_sw_filter)
    
response_all = xmltodict.parse(ncclient_response.xml)
pprint.pprint(response_all)

response_spec = xmltodict.parse(ncclient_response.xml)['rpc-reply']['data']
inv = response_spec['device-hardware-data']['device-hardware']['device-inventory']
sys = response_spec['device-hardware-data']['device-hardware']['device-system-data']

print("\n\nSerial number = " + inv['serial-number'])
print("\n\nSoftware version: \n" + sys['software-version'])
print(type(sys['software-version']))

"""
(env-scrapli) gandalf@debian11:~/Python/scrapli-yang$ python3 05_parse-sn.py 
{'rpc-reply': {'@message-id': 'urn:uuid:8d6978b6-a3c4-49fe-bdac-e03268e52014',
               '@xmlns': 'urn:ietf:params:xml:ns:netconf:base:1.0',
               '@xmlns:nc': 'urn:ietf:params:xml:ns:netconf:base:1.0',
               'data': {'device-hardware-data': {'@xmlns': 'http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper',
                                                 'device-hardware': {'device-inventory': {'hw-description': 'Cisco '
                                                                                                            'CSR1000V '
                                                                                                            'Chassis',
                                                                                          'hw-dev-index': '0',
                                                                                          'hw-type': 'hw-type-chassis',
                                                                                          'part-number': 'CSR1000V',
                                                                                          'serial-number': '94N9U8ZRS16',
                                                                                          'version': 'V00'},
                                                                     'device-system-data': {'boot-time': '2023-10-15T16:23:19+00:00',
                                                                                            'current-time': '2023-10-15T19:37:49+00:00',
                                                                                            'last-reboot-reason': 'reload',
                                                                                            'rommon-version': 'IOS-XE '
                                                                                                              'ROMMON',
                                                                                            'software-version': 'Cisco '
                                                                                                                'IOS '
                                                                                                                'Software '
                                                                                                                '[Fuji], '
                                                                                                                'Virtual '
                                                                                                                'XE '
                                                                                                                'Software '
                                                                                                                '(X86_64_LINUX_IOSD-UNIVERSALK9-M), '
                                                                                                                'Version '
                                                                                                                '16.9.7, '
                                                                                                                'RELEASE '
                                                                                                                'SOFTWARE '
                                                                                                                '(fc1)\n'
                                                                                                                'Technical '
                                                                                                                'Support: '
                                                                                                                'http://www.cisco.com/techsupport\n'
                                                                                                                'Copyright '
                                                                                                                '(c) '
                                                                                                                '1986-2021 '
                                                                                                                'by '
                                                                                                                'Cisco '
                                                                                                                'Systems, '
                                                                                                                'Inc.\n'
                                                                                                                'Compiled '
                                                                                                                'Wed '
                                                                                                                '10-Feb-21 '
                                                                                                                '09:14 '
                                                                                                                'by '
                                                                                                                'mcpre'}}}}}}


Serial number = 94N9U8ZRS16


Software version: 
Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.7, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2021 by Cisco Systems, Inc.
Compiled Wed 10-Feb-21 09:14 by mcpre
<class 'str'>
"""

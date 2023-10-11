from scrapli_netconf.driver import NetconfDriver

device = {
    "host": "192.168.100.13",
    "auth_username": "gandalf",
    "auth_password": "grey",
    "auth_strict_key": False,
    "port": 830,    
    "transport_options": {"open_cmd": ["-o", "KexAlgorithms=+diffie-hellman-group-exchange-sha1", "-o", "Ciphers=+aes256-cbc"]}
}

conn = NetconfDriver(**device)
conn.open()

sn_filter = """
<device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper">
    <device-hardware>
        <device-inventory>
            <hw-type>hw-type-chassis</hw-type>
            <hw-dev-index>0</hw-dev-index>
            <serial-number></serial-number>
        </device-inventory>
    </device-hardware>
</device-hardware-data>
"""

response = conn.get(
    filter_=sn_filter, filter_type='subtree')
print(response.result)

"""
YANG MODEL:

gandalf@debian11:~/yang/vendor/cisco/xe/1693$ pyang -f tree Cisco-IOS-XE-device-hardware-oper.yang

module: Cisco-IOS-XE-device-hardware-oper
  +--ro device-hardware-data
     +--ro device-hardware!
        +--ro device-inventory* [hw-type hw-dev-index]
        |  +--ro hw-type           device-hardware-xe-oper:hw-type
        |  +--ro hw-dev-index      uint32
        |  +--ro version?          string
        |  +--ro part-number?      string
        |  +--ro serial-number?    string
        |  +--ro hw-description?   string
        +--ro device-alarm* [alarm-id alarm-instance]
        |  +--ro alarm-id             uint32
        |  +--ro alarm-instance       uint32
        |  +--ro alarm-name?          string
        |  +--ro alarm-category?      device-hardware-xe-oper:alarm-severity
        |  +--ro alarm-time?          yang:date-and-time
        |  +--ro alarm-description?   string
        +--ro device-system-data!
           +--ro current-time?         yang:date-and-time
           +--ro boot-time?            yang:date-and-time
           +--ro software-version?     string
           +--ro rommon-version?       string
           +--ro last-reboot-reason?   string
gandalf@debian11:~/yang/vendor/cisco/xe/1693$

"""

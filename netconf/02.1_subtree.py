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
    </device-hardware>
</device-hardware-data>
"""

response = conn.get(
    filter_=sn_filter, filter_type='subtree')
print(response.result)

"""
OUTPUT:

(env-scrapli) gandalf@debian11:~/Python/scrapli-yang$ python3 02_subtree.py 
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <data>
    <device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper">
      <device-hardware>
        <device-inventory>
          <hw-type>hw-type-chassis</hw-type>
          <hw-dev-index>0</hw-dev-index>
          <version>V00</version>
          <part-number>CSR1000V</part-number>
          <serial-number>94N9U8ZRS16</serial-number>
          <hw-description>Cisco CSR1000V Chassis</hw-description>
        </device-inventory>
        <device-inventory>
          <hw-type>hw-type-pim</hw-type>
          <hw-dev-index>1</hw-dev-index>
          <version>V00</version>
          <part-number>CSR1000V</part-number>
          <serial-number>JAB1303001C</serial-number>
          <hw-description>Cisco CSR1000V Route Processor</hw-description>
        </device-inventory>
        <device-inventory>
          <hw-type>hw-type-pim</hw-type>
          <hw-dev-index>2</hw-dev-index>
          <version/>
          <part-number>CSR1000V</part-number>
          <serial-number/>
          <hw-description>Cisco CSR1000V Embedded Services Processor</hw-description>
        </device-inventory>
        <device-inventory>
          <hw-type>hw-type-dram</hw-type>
          <hw-dev-index>3</hw-dev-index>
          <version/>
          <part-number/>
          <serial-number/>
          <hw-description>Physical Memory</hw-description>
        </device-inventory>
        <device-inventory>
          <hw-type>hw-type-cpu</hw-type>
          <hw-dev-index>4</hw-dev-index>
          <version> 6</version>
          <part-number> GenuineIntel</part-number>
          <serial-number/>
          <hw-description> Intel Core i7 9xx (Nehalem Class Core </hw-description>
        </device-inventory>
        <device-system-data>
          <current-time>2023-10-15T17:31:29+00:00</current-time>
          <boot-time>2023-10-15T16:23:20+00:00</boot-time>
          <software-version>Cisco IOS Software [Fuji], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.7, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2021 by Cisco Systems, Inc.
Compiled Wed 10-Feb-21 09:14 by mcpre</software-version>
          <rommon-version>&#13;
IOS-XE ROMMON
</rommon-version>
          <last-reboot-reason>reload</last-reboot-reason>
        </device-system-data>
      </device-hardware>
    </device-hardware-data>
  </data>
</rpc-reply>
"""

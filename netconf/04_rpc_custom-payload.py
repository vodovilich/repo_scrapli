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

rpc_filter = '''
<get>
<filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper" type="xpath" select="/device-hardware-data/device-hardware/device-inventory[hw-type='hw-type-chassis']/serial-number" /> 
</get>
'''
response = conn.rpc(rpc_filter)
print(response.result)

"""
(env-scrapli) gandalf@debian11:~/Python/scrapli-yang$ python3 04_rpc_custom-payload.py 
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <data>
    <device-hardware-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-device-hardware-oper">
      <device-hardware>
        <device-inventory>
          <hw-type>hw-type-chassis</hw-type>
          <hw-dev-index>0</hw-dev-index>
          <serial-number>94N9U8ZRS16</serial-number>
        </device-inventory>
      </device-hardware>
    </device-hardware-data>
  </data>
</rpc-reply>
"""

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

xpath = '/device-hardware-data/device-hardware/device-inventory[hw-type="hw-type-chassis"]'

response = conn.get(
    filter_=xpath, filter_type='xpath')
print(response.result)

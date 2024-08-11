from scrapli_netconf.driver import NetconfDriver
import yaml

with open('secret.yml', 'r') as f:
    secret_dick = yaml.safe_load(f)
NETCONF_USER = secret_dick['USERNAME']
NETCONF_PAS = secret_dick['PASSWORD']

with open('devs.yml','r') as f:
    dev_list = yaml.safe_load(f)



def get_xpath(dev):

    XPATH_EXPRESSION = '/device-hardware-data/device-hardware/device-inventory[hw-type="hw-type-chassis"]'

    device = {
        'host': dev,
        'auth_username': NETCONF_USER,
        'auth_password': NETCONF_PAS,
        'auth_strict_key': False,
        'port': 830,
        'transport_options': {'open_cmd': ['-o', 'KexAlgorithms=+diffie-hellman-group-exchange-sha1', '-o', 'Ciphers=+aes256-cbc'] }
    }

    conn = NetconfDriver(**device, timeout_ops=20, timeout_transport=20, transport='ssh2')
    conn.open()

    response = conn.get(filter_=XPATH_EXPRESSION, filter_type='xpath')
    print(response.result)

if __name__ == '__main__':
    for target in dev_list:
        get_xpath(target)

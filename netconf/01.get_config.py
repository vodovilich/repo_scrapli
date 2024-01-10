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
response = conn.get_config(source="running")
print(response.result)
print("hui")



"""
(env-scrapli) gandalf@debian11:~/Python/scrapli-yang$ python3 01.get_config.py 
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="101">
  <data>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <version>16.9</version>
      <boot-start-marker/>
      <boot-end-marker/>
      <service>
        <timestamps>
          <debug>
            <datetime>
              <msec/>
            </datetime>
          </debug>
          <log>
            <datetime>
              <msec/>
            </datetime>
          </log>
        </timestamps>
        <config/>
      </service>
      <platform>
        <console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
          <output>serial</output>
        </console>
        <punt-keepalive xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
          <disable-kernel-core>true</disable-kernel-core>
        </punt-keepalive>
      </platform>
      <hostname>csr1000v-01</hostname>
      <archive>
        <log>
          <config>
            <hidekeys/>
            <logging>
              <enable/>
            </logging>
          </config>
        </log>
      </archive>
      <username>
        <name>csruser</name>
        <privilege>15</privilege>
        <secret>
          <encryption>5</encryption>
          <secret>$1$7meO$s/2HE8VKDD9Lg08IGLw3H1</secret>
        </secret>
      </username>
      <username>
        <name>gandalf</name>
        <privilege>15</privilege>
        <secret>
          <encryption>5</encryption>
          <secret>$1$lPHt$CWhW4arVvOrWfvKEiZnCB1</secret>
        </secret>
      </username>
      <ip>
        <domain>
          <name>atffc.hui</name>
        </domain>
        <forward-protocol>
          <protocol>nd</protocol>
        </forward-protocol>
        <scp>
          <server>
            <enable/>
          </server>
        </scp>
        <ssh>
          <pubkey-chain>
            <username>
              <name>frodo</name>
              <key-hash>
                <key-type>ssh-rsa</key-type>
                <key-hash-value>9E0422426EA11A0679430801859CF5B6</key-hash-value>
              </key-hash>
            </username>
          </pubkey-chain>
        </ssh>
        <access-list>
          <extended xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-acl">
            <name>rfc1918-in-acl</name>
            <access-list-seq-rule>
              <sequence>10</sequence>
              <ace-rule>
                <action>deny</action>
                <protocol>ip</protocol>
                <ipv4-address>10.0.0.0</ipv4-address>
                <mask>0.255.255.255</mask>
                <dst-any/>
              </ace-rule>
            </access-list-seq-rule>
            <access-list-seq-rule>
              <sequence>20</sequence>
              <ace-rule>
                <action>deny</action>
                <protocol>ip</protocol>
                <ipv4-address>172.16.0.0</ipv4-address>
                <mask>0.15.255.255</mask>
                <dst-any/>
              </ace-rule>
            </access-list-seq-rule>
            <access-list-seq-rule>
              <sequence>30</sequence>
              <ace-rule>
                <action>deny</action>
                <protocol>ip</protocol>
                <ipv4-address>192.168.0.0</ipv4-address>
                <mask>0.0.255.255</mask>
                <dst-any/>
              </ace-rule>
            </access-list-seq-rule>
            <access-list-seq-rule>
              <sequence>40</sequence>
              <ace-rule>
                <action>permit</action>
                <protocol>ip</protocol>
                <any/>
                <dst-any/>
              </ace-rule>
            </access-list-seq-rule>
          </extended>
        </access-list>
        <http xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-http">
          <authentication>
            <local/>
          </authentication>
          <server>true</server>
          <secure-server>true</secure-server>
          <client>
            <source-interface>GigabitEthernet1</source-interface>
          </client>
        </http>
      </ip>
      <interface>
        <GigabitEthernet>
          <name>1</name>
          <ip>
            <address>
              <dhcp/>
            </address>
          </ip>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
        <GigabitEthernet>
          <name>2</name>
          <shutdown/>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
        <GigabitEthernet>
          <name>3</name>
          <shutdown/>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
        <GigabitEthernet>
          <name>4</name>
          <shutdown/>
          <mop>
            <enabled>false</enabled>
            <sysid>false</sysid>
          </mop>
          <negotiation xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ethernet">
            <auto>true</auto>
          </negotiation>
        </GigabitEthernet>
        <Loopback>
          <name>0</name>
          <ip>
            <address>
              <primary>
                <address>192.168.255.30</address>
                <mask>255.255.255.255</mask>
              </primary>
            </address>
          </ip>
        </Loopback>
      </interface>
      <control-plane/>
      <logging>
        <buffered>
          <size>
            <size-value>65432</size-value>
          </size>
        </buffered>
      </logging>
      <login>
        <on-success>
          <log/>
        </on-success>
      </login>
      <multilink>
        <bundle-name xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ppp">authenticated</bundle-name>
      </multilink>
      <redundancy/>
      <spanning-tree>
        <extend xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-spanning-tree">
          <system-id/>
        </extend>
      </spanning-tree>
      <subscriber>
        <templating/>
      </subscriber>
      <crypto>
        <pki xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-crypto">
          <trustpoint>
            <id>TP-self-signed-743765055</id>
            <enrollment>
              <selfsigned/>
            </enrollment>
            <revocation-check>none</revocation-check>
            <rsakeypair>
              <key-label>TP-self-signed-743765055</key-label>
            </rsakeypair>
            <subject-name>cn=IOS-Self-Signed-Certificate-743765055</subject-name>
          </trustpoint>
          <certificate>
            <chain>
              <name>TP-self-signed-743765055</name>
              <certificate>
                <serial>01</serial>
                <certtype>self-signed</certtype>
              </certificate>
            </chain>
          </certificate>
        </pki>
      </crypto>
      <router>
        <bgp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp">
          <id>65001</id>
          <bgp>
            <log-neighbor-changes>true</log-neighbor-changes>
          </bgp>
          <neighbor>
            <id>192.168.100.6</id>
            <remote-as>65001</remote-as>
          </neighbor>
          <neighbor>
            <id>192.168.100.7</id>
            <remote-as>65001</remote-as>
          </neighbor>
        </bgp>
      </router>
      <license>
        <udi>
          <pid>CSR1000V</pid>
          <sn>94N9U8ZRS16</sn>
        </udi>
      </license>
      <line>
        <console>
          <first>0</first>
          <stopbits>1</stopbits>
        </console>
        <vty>
          <first>0</first>
          <last>4</last>
          <login>
            <local/>
          </login>
          <transport>
            <input>
              <input>ssh</input>
            </input>
          </transport>
        </vty>
        <vty>
          <first>5</first>
          <last>15</last>
          <login>
            <local/>
          </login>
          <transport>
            <input>
              <input>ssh</input>
            </input>
          </transport>
        </vty>
      </line>
      <ntp>
        <server xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ntp">
          <server-list>
            <ip-address>2.3.4.5</ip-address>
          </server-list>
        </server>
      </ntp>
      <diagnostic xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-diagnostics">
        <bootup>
          <level>minimal</level>
        </bootup>
      </diagnostic>
    </native>
    <licensing xmlns="http://cisco.com/ns/yang/cisco-smart-license">
      <config>
        <enable>false</enable>
        <privacy>
          <hostname>false</hostname>
          <version>false</version>
        </privacy>
        <utility>
          <utility-enable>false</utility-enable>
        </utility>
      </config>
    </licensing>
    <acl xmlns="http://openconfig.net/yang/acl">
      <acl-sets>
        <acl-set>
          <name>rfc1918-in-acl</name>
          <type>ACL_IPV4</type>
          <config>
            <name>rfc1918-in-acl</name>
            <type>ACL_IPV4</type>
          </config>
          <acl-entries>
            <acl-entry>
              <sequence-id>10</sequence-id>
              <config>
                <sequence-id>10</sequence-id>
              </config>
              <ipv4>
                <config>
                  <source-address>10.0.0.0/8</source-address>
                  <protocol xmlns:oc-acl-cisco="http://cisco.com/ns/yang/cisco-xe-openconfig-acl-ext">oc-acl-cisco:IP</protocol>
                </config>
              </ipv4>
              <transport>
                <config>
                  <source-port>ANY</source-port>
                  <destination-port>ANY</destination-port>
                </config>
              </transport>
              <actions>
                <config>
                  <forwarding-action>DROP</forwarding-action>
                  <log-action>LOG_NONE</log-action>
                </config>
              </actions>
            </acl-entry>
            <acl-entry>
              <sequence-id>20</sequence-id>
              <config>
                <sequence-id>20</sequence-id>
              </config>
              <ipv4>
                <config>
                  <source-address>172.16.0.0/12</source-address>
                  <protocol xmlns:oc-acl-cisco="http://cisco.com/ns/yang/cisco-xe-openconfig-acl-ext">oc-acl-cisco:IP</protocol>
                </config>
              </ipv4>
              <transport>
                <config>
                  <source-port>ANY</source-port>
                  <destination-port>ANY</destination-port>
                </config>
              </transport>
              <actions>
                <config>
                  <forwarding-action>DROP</forwarding-action>
                  <log-action>LOG_NONE</log-action>
                </config>
              </actions>
            </acl-entry>
            <acl-entry>
              <sequence-id>30</sequence-id>
              <config>
                <sequence-id>30</sequence-id>
              </config>
              <ipv4>
                <config>
                  <source-address>192.168.0.0/16</source-address>
                  <protocol xmlns:oc-acl-cisco="http://cisco.com/ns/yang/cisco-xe-openconfig-acl-ext">oc-acl-cisco:IP</protocol>
                </config>
              </ipv4>
              <transport>
                <config>
                  <source-port>ANY</source-port>
                  <destination-port>ANY</destination-port>
                </config>
              </transport>
              <actions>
                <config>
                  <forwarding-action>DROP</forwarding-action>
                  <log-action>LOG_NONE</log-action>
                </config>
              </actions>
            </acl-entry>
            <acl-entry>
              <sequence-id>40</sequence-id>
              <config>
                <sequence-id>40</sequence-id>
              </config>
              <ipv4>
                <config>
                  <protocol xmlns:oc-acl-cisco="http://cisco.com/ns/yang/cisco-xe-openconfig-acl-ext">oc-acl-cisco:IP</protocol>
                </config>
              </ipv4>
              <transport>
                <config>
                  <source-port>ANY</source-port>
                  <destination-port>ANY</destination-port>
                </config>
              </transport>
              <actions>
                <config>
                  <forwarding-action>ACCEPT</forwarding-action>
                  <log-action>LOG_NONE</log-action>
                </config>
              </actions>
            </acl-entry>
          </acl-entries>
        </acl-set>
      </acl-sets>
    </acl>
    <interfaces xmlns="http://openconfig.net/yang/interfaces">
      <interface>
        <name>GigabitEthernet1</name>
        <config>
          <name>GigabitEthernet1</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <enabled>true</enabled>
        </config>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <config>
              <index>0</index>
              <enabled>true</enabled>
            </config>
            <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
              <config>
                <enabled>false</enabled>
              </config>
            </ipv6>
          </subinterface>
        </subinterfaces>
        <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
          <config>
            <mac-address>50:00:00:06:00:00</mac-address>
            <auto-negotiate>true</auto-negotiate>
          </config>
        </ethernet>
      </interface>
      <interface>
        <name>GigabitEthernet2</name>
        <config>
          <name>GigabitEthernet2</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <enabled>false</enabled>
        </config>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <config>
              <index>0</index>
              <enabled>false</enabled>
            </config>
            <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
              <config>
                <enabled>false</enabled>
              </config>
            </ipv6>
          </subinterface>
        </subinterfaces>
        <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
          <config>
            <mac-address>50:00:00:06:00:01</mac-address>
            <auto-negotiate>true</auto-negotiate>
          </config>
        </ethernet>
      </interface>
      <interface>
        <name>GigabitEthernet3</name>
        <config>
          <name>GigabitEthernet3</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <enabled>false</enabled>
        </config>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <config>
              <index>0</index>
              <enabled>false</enabled>
            </config>
            <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
              <config>
                <enabled>false</enabled>
              </config>
            </ipv6>
          </subinterface>
        </subinterfaces>
        <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
          <config>
            <mac-address>50:00:00:06:00:02</mac-address>
            <auto-negotiate>true</auto-negotiate>
          </config>
        </ethernet>
      </interface>
      <interface>
        <name>GigabitEthernet4</name>
        <config>
          <name>GigabitEthernet4</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <enabled>false</enabled>
        </config>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <config>
              <index>0</index>
              <enabled>false</enabled>
            </config>
            <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
              <config>
                <enabled>false</enabled>
              </config>
            </ipv6>
          </subinterface>
        </subinterfaces>
        <ethernet xmlns="http://openconfig.net/yang/interfaces/ethernet">
          <config>
            <mac-address>50:00:00:06:00:03</mac-address>
            <auto-negotiate>true</auto-negotiate>
          </config>
        </ethernet>
      </interface>
      <interface>
        <name>Loopback0</name>
        <config>
          <name>Loopback0</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
          <enabled>true</enabled>
        </config>
        <subinterfaces>
          <subinterface>
            <index>0</index>
            <config>
              <index>0</index>
              <enabled>true</enabled>
            </config>
            <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
              <addresses>
                <address>
                  <ip>192.168.255.30</ip>
                  <config>
                    <ip>192.168.255.30</ip>
                    <prefix-length>32</prefix-length>
                  </config>
                </address>
              </addresses>
            </ipv4>
            <ipv6 xmlns="http://openconfig.net/yang/interfaces/ip">
              <config>
                <enabled>false</enabled>
              </config>
            </ipv6>
          </subinterface>
        </subinterfaces>
      </interface>
    </interfaces>
    <network-instances xmlns="http://openconfig.net/yang/network-instance">
      <network-instance>
        <name>default</name>
        <config>
          <name>default</name>
          <type xmlns:oc-ni-types="http://openconfig.net/yang/network-instance-types">oc-ni-types:DEFAULT_INSTANCE</type>
          <description>default-vrf [read-only]</description>
        </config>
        <tables>
          <table>
            <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
            <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
            <config>
              <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
              <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
            </config>
          </table>
          <table>
            <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
            <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
            <config>
              <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</protocol>
              <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
            </config>
          </table>
          <table>
            <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
            <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
            <config>
              <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
              <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV4</address-family>
            </config>
          </table>
          <table>
            <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
            <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
            <config>
              <protocol xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</protocol>
              <address-family xmlns:oc-types="http://openconfig.net/yang/openconfig-types">oc-types:IPV6</address-family>
            </config>
          </table>
        </tables>
        <protocols>
          <protocol>
            <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP</identifier>
            <name>65001</name>
            <config>
              <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:BGP</identifier>
              <name>65001</name>
            </config>
            <bgp>
              <global>
                <config>
                  <as>65001</as>
                </config>
                <graceful-restart>
                  <config>
                    <enabled>false</enabled>
                  </config>
                </graceful-restart>
                <route-selection-options>
                  <config>
                    <always-compare-med>false</always-compare-med>
                    <external-compare-router-id>false</external-compare-router-id>
                  </config>
                </route-selection-options>
              </global>
              <neighbors>
                <neighbor>
                  <neighbor-address>192.168.100.6</neighbor-address>
                  <config>
                    <neighbor-address>192.168.100.6</neighbor-address>
                    <peer-as>65001</peer-as>
                  </config>
                  <timers>
                    <config>
                      <hold-time>180.0</hold-time>
                      <keepalive-interval>60.0</keepalive-interval>
                    </config>
                  </timers>
                  <ebgp-multihop>
                    <config>
                      <enabled>true</enabled>
                    </config>
                  </ebgp-multihop>
                </neighbor>
                <neighbor>
                  <neighbor-address>192.168.100.7</neighbor-address>
                  <config>
                    <neighbor-address>192.168.100.7</neighbor-address>
                    <peer-as>65001</peer-as>
                  </config>
                  <timers>
                    <config>
                      <hold-time>180.0</hold-time>
                      <keepalive-interval>60.0</keepalive-interval>
                    </config>
                  </timers>
                  <ebgp-multihop>
                    <config>
                      <enabled>true</enabled>
                    </config>
                  </ebgp-multihop>
                </neighbor>
              </neighbors>
            </bgp>
          </protocol>
          <protocol>
            <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</identifier>
            <name>DEFAULT</name>
            <config>
              <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:STATIC</identifier>
              <name>DEFAULT</name>
            </config>
          </protocol>
          <protocol>
            <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</identifier>
            <name>DEFAULT</name>
            <config>
              <identifier xmlns:oc-pol-types="http://openconfig.net/yang/policy-types">oc-pol-types:DIRECTLY_CONNECTED</identifier>
              <name>DEFAULT</name>
            </config>
          </protocol>
        </protocols>
      </network-instance>
    </network-instances>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet1</name>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
      <interface>
        <name>GigabitEthernet2</name>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>false</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
      <interface>
        <name>GigabitEthernet3</name>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>false</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
      <interface>
        <name>GigabitEthernet4</name>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>false</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
      <interface>
        <name>Loopback0</name>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
          <address>
            <ip>192.168.255.30</ip>
            <netmask>255.255.255.255</netmask>
          </address>
        </ipv4>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
    </interfaces>
    <nacm xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-acm">
      <enable-nacm>true</enable-nacm>
      <read-default>deny</read-default>
      <write-default>deny</write-default>
      <exec-default>deny</exec-default>
      <enable-external-groups>true</enable-external-groups>
      <rule-list>
        <name>admin</name>
        <group>PRIV15</group>
        <rule>
          <name>permit-all</name>
          <module-name>*</module-name>
          <access-operations>*</access-operations>
          <action>permit</action>
        </rule>
      </rule-list>
    </nacm>
    <routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
      <routing-instance>
        <name>default</name>
        <description>default-vrf [read-only]</description>
        <routing-protocols>
          <routing-protocol>
            <type>static</type>
            <name>1</name>
          </routing-protocol>
        </routing-protocols>
      </routing-instance>
    </routing>
  </data>
</rpc-reply>

hui
"""

import os
import paramiko

target= raw_input("Masukkan Target : ")
user= raw_input("Masukkan user : ")
passwd=raw_input("Masukkan Password : ")
portnya=raw_input("Masukkan Portnya : ")

scpnya = '''sshpass -p '{}' scp -P {} -o StrictHostKeyChecking=no -r hotspotku {}@{}:/'''.format(passwd,portnya,user,target)
os.system(scpnya)
konfig = '''
:global intlan [/ip address get [/ip address find address~"192"] interface]
:global pool  [ip dhcp-server get [/ip dhcp-server find interface=$intlan] address-pool ]
:global iplan [/ip address get [find interface=$intlan] address]
:set iplan [:pick $iplan 0 [:find $iplan "/" -1]]
/ip hotspot profile add hotspot-address=$iplan name="hs-$intlan" html-directory=hotspotku
/ip hotspot add address-pool=$pool interface=$intlan name="hs-$intlan" profile="hs-$intlan" disabled=no
/ip hotspot user add name=free password=free
/system identity print
/ip hotspot export
'''

dssh = paramiko.SSHClient()
dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
dssh.connect(target, port=portnya, username=user, password=passwd)
stdin, stdout, stderr= dssh.exec_command(konfig)
print "===================================="
print "Berikut Lognya :"
print "===================================="
print stdout.read()
print "===================================="
print "Aceng'WH @ 2020"

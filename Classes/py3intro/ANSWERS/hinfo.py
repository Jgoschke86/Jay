#!/usr/bin/python3
# one data record:
# aquila:Solaris:10:Sparc:elx0/11.1.3.10;elx0/11.1.14.37:200000:4096:Porky Pig

host_info_for = {}
with open('../DATA/systems.dat') as SYS:
    for rec in SYS:
        (host,os,version,arch,ifaces,hdrives,mem,user) = rec[:-1].split(':')
        host_info_for[host] = { 'OS':os, 'OS_VERSION':version,
         'ARCHITECTURE':arch, 'NET_IFACE':ifaces.split(';'), 
         'HARD_DRIVES':hdrives.split(','), 'MEMORY':mem, 'USER':user }

output_format = '\t{0:25s} {1}'
while True:
    hostname = input("Enter host name or q to quit: ")
    if hostname.lower() == 'q':
        break
    if hostname == '':
        continue
    
    if hostname in host_info_for:
        print(hostname + ':')
        h = host_info_for[hostname]
        print(output_format.format('Operating System',h['OS']))
        print(output_format.format('OS Version',h['OS_VERSION']))
        print(output_format.format('Architecture',h['ARCHITECTURE']))
        print(output_format.format('Network Interfaces',' '.join(h['NET_IFACE'])))
        print(output_format.format('Hard Drives',' '.join(h['HARD_DRIVES'])))
        print(output_format.format('Memory (GB)',h['MEMORY']))
        print(output_format.format('User',h['USER']))
    else:
        print("Sorry, that host does not exist\n")
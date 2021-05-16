##Testing Getting IP Address
import socket

system_ip_address = socket.gethostbyname(socket.gethostname())
print("System IP Address:",system_ip_address)

system_hostname = socket.gethostname()
print("Hotname:",system_hostname)

'Resolve DNS'
dns_name = socket.gethostbyaddr("172.16.5.200")
print("172.16.5.200 resolved to:",dns_name[0].strip())
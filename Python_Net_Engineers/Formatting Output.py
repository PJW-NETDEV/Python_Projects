
#Printing Muliple Variables
ip_addr1 = "172.16.1.1"
ip_addr2 = "192.168.5.200"
ip_addr3 = "10.10.50.1"
port1 = "80"
port2 = "443"
port3 = "53"

print(ip_addr1,ip_addr2,ip_addr3)

#Creating a benner, repeating strings
print("\n" *2)
print("-" * 100)
print("---"," Welcome to my script", " ---")
print("-" * 100)
print("\n" *2)

# Formatting
print()
print("Formatting output.","\n")
print("Basic assignment of variables to format sections")
print("{}{}{}".format(ip_addr1,ip_addr2,ip_addr3))
print()
print("Format To Columns 20 chars in length")
print("{:20}{:20}{:20}".format(ip_addr1,ip_addr2,ip_addr3))
print()
print("Format To Columns 20 chars in length and right alligned")
print("{:>20}{:>20}{:>20}".format(ip_addr1,ip_addr2,ip_addr3))
print()
print("Format To Columns 20 chars in length and Centered")
print("{:^20}{:^20}{:^20}".format(ip_addr1,ip_addr2,ip_addr3))

###Formating using named arguments
print()
print("Formating using named arguments")
print("{my_ip_1:^20}{my_ip_2:^20}{my_ip_3:^20}".format(my_ip_3=ip_addr1,my_ip_2=ip_addr2,my_ip_1=ip_addr3))

##Formating Using List
print()
#Create list variable called Octents
octets = ip_addr1.split(".")
print("Formatting Output Using List - manual assignment")
#print(octets[0])
print("{:^20}{:^20}{:^20}{:^20}".format(octets[0],octets[1],octets[2],octets[3]))

#Create list variable called Octets
octets = ip_addr1.split(".")
print("Formatting Output Using List - auto assignment")
print("{:^20}{:^20}{:^20}{:^20}".format(*octets))

#Printing Using Print-F Function - only in 3.6.2 or higher
#Allows formatting referenced in place
print()
print("Formatting inline")
print(f"Host 1 is on IP Address: {ip_addr1:<20} on Port: {port1:<5}")
print(f"Host 2 is on IP Address: {ip_addr2:<20} on Port: {port2:<5}")
print(f"Host 3 is on IP Address: {ip_addr3:<20} on Port: {port3:<5}")

print("\n"*2)
print("Testing Table")
hostname1 = "Host 1 is on IP: "
hostname2 = "Host 1 is on IP: "
hostname3 = "Host 1 is on IP: "
print(f"{hostname1:>20} {ip_addr1:<20} on Port: {port1:<5}")
print(f"{hostname2:>20} {ip_addr1:<20} on Port: {port1:<5}")
print(f"{hostname3:>20} {ip_addr1:<20} on Port: {port1:<5}")

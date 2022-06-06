#Script Written By
#Gaurav Aggarwal
#Dated - 06-06-2022
#Description - Script takes ipv4 and ipv6 addresses to ping from a file named inputs , validates the IPs and then ping
#               gives a ping result in a result.txt file in the same python directory
#contact - for any issues please contact me_gauravaggarwal@yahoo.com

import re
import os

file_exists = os.path.exists('inputs.txt')
if (file_exists):
    with open('inputs.txt') as fh:
        string = fh.readlines()
        print(string)
else:
    print('Input file with name Input_IPs.txt not found in program directory.')

def Validate_ip(ip):
    regex_v4 = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|" \
               "2[0-4][0-9]|25[0-5])\\.){3}" \
               "([0-9]|[1-9][0-9]|1[0-9][0-9]|" \
               "2[0-4][0-9]|25[0-5])"

    regex_v6 = "/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$|^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$|^(?:(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){6})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:::(?:(?:(?:[0-9a-fA-F]{1,4})):){5})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){4})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,1}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){3})" \
               "(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:" \
               "[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,2}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){2})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,3}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:[0-9a-fA-F]{1,4})):)(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,4}(?:(?:[0-9a-fA-F]{1,4})))?::)(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,5}(?:(?:[0-9a-fA-F]{1,4})))?::)" \
               "(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,6}(?:(?:[0-9a-fA-F]{1,4})))?::))))$"

    pattern_v4 = re.compile(regex_v4)
    pattern_v6 = re.compile(regex_v6)

    if(re.fullmatch(pattern_v4,ip)):
        flag="ipv4"
        return(flag)
    elif(re.fullmatch(pattern_v6,ip)):
        flag="ipv6"
        return(flag)
    else:
        flag="invalid"
        return(flag)

valid_v4 = []
valid_v6 = []
invalid = []

for line in string:
    line=line.rstrip()
    result= Validate_ip(line)

    if(result=="ipv4"):
        valid_v4.append(line)
    elif (result=="ipv6"):
        valid_v6.append(line)
    elif(result=="invalid"):
        invalid.append(line)

valid = valid_v4 + valid_v6

OS_TYPE = os.name
# Sets the count modifier to the os type
COUNT = '-n' if OS_TYPE == 'nt' else '-c'

results_file = open("results.txt", "w")

for ip in valid:
    response = os.popen(f"ping {ip} {COUNT} 1").read()
    if "Received = 1" in response and "Approximate" in response:
        print(f"UP {ip} Ping Successful")
        results_file.write(f"UP {ip} Ping Successful" + "\n")
    else:
        print(f"Down {ip} Ping Unsuccessful")
        results_file.write(f"Down {ip} Ping Unsuccessful" + "\n")

for ip in invalid:
    print(f"invalid {ip} Ping not done")
    results_file.write(f"Invalid {ip} Ping Not Done" + "\n")

results_file.close()

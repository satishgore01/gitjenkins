import yaml
import ipaddress
import os
import time


print("collecting host data......." + "\n")
print("###########")
print("##########")


OSfile = ".sampleos.yml"
inventory = ".inventory_sample.yml"
file_path = "input.txt"
lines = []
file_name = ".variable.txt"

os.remove(file_name)

def textcreate(name):
    with open(file_name, 'a') as file:
    # Write the output to the file
        file.write(str(name) + '\n')



def rcidrgen(v1,v2,v3):
    subnet = v1
    vlan = v2
    hostid = v3
    suffix = "::/112"
    suffix2= "::"
    groups = subnet.split(":")
    hostidd = hostid.split(":")
    host = hostidd[:2]
    host2 = ":".join(host)
    groups[-1] = str(vlan)
    rcidr = ":".join(groups)
    RCIDR = rcidr + ":" + host2 + suffix
    serv_prefix = rcidr
    textcreate(serv_prefix)
    Rvip  = rcidr + ":" + host2 + suffix2
   # print(RCIDR)
    textcreate(RCIDR)
   # print(Rvip)
    textcreate(Rvip)






def ipgennrator():

    file_path = "input.txt"  # Replace with the actual file path
try:
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them in an array (list)
        lines = file.readlines()
except FileNotFoundError:
      # print(f"File not found: {file_path}")
    lines = []
# Print the content of the array (list)
for line in lines:
     print(line.strip())  # .strip() removes leading/trailing whitespace and
lines = [item.replace("\n", "") for item in lines]

BMC = lines[2]
HOST = lines[3]

for i in range(8):
    textcreate(lines[i])

ipv6_address=BMC
# Parse the IPv6 address
for i in range (2):
  ip = ipaddress.IPv6Address(ipv6_address)
  parts = ipv6_address.split(':')
  desired_part = ':'.join(parts[4:])
  parts = ipv6_address.split(':')
  subnet = ':'.join(parts[:4])
  vlan  = parts[3]
  rnic  = f"bond0:{vlan}:untagged"

  textcreate(subnet)
  textcreate(rnic)
 # print("id:",desired_part)
  textcreate(desired_part)
  ipv6_address=HOST

rcidrgen(subnet,lines[6],desired_part)
textcreate(OSfile)
textcreate(inventory)

def loadingfile():
    print("#########################################################")
    print("#########################################################")



#ganerating varible file 
ipgennrator()



# Open the text file in read mode
file_path = ".variable.txt"
try:
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them in an array (list)
        lines = file.readlines()
except FileNotFoundError:
   # print(f"File not found: {file_path}")
    lines = []

# Print the content of the array (list)
for line in lines:
   print(line.strip())  # .strip() removes leading/trailing whitespace and

lines = [item.replace("\n", "") for item in lines]




new_hostname = lines[0]
RCP = lines[1]
BMC_ip = lines[2]
host_ip = lines[3]
ServerKind = lines[4]
Robin_version= lines[5]
S_vlan = lines[6]
server_vlan = int(S_vlan)
Rcpdc= lines[7]
BMC_prefix = lines[8]
BMC_ID = lines[10]
host_prefix = lines[11]
Host_ID = lines[13]
R_nics= lines[12]
serv_pre = lines[14]
CIDR = lines[15]
RVIP = lines[16]
os_path = lines[17]
input_yaml_path = os_path



print("host data collected......." + "\n")
print("###########")
print("##########")



print("Ganerating OS ymal file.....")
loadingfile()




parent_dir = "/home/kube/ymlfiles"
path =  os.path.join(parent_dir, new_hostname)

try:
   os.mkdir(path)
except FileExistsError:
    print("directory exist")



print(path)
outputfile = path + "/"  + "os_install_" + new_hostname + ".yaml"
output_yaml_path = outputfile


# Load the original YAML file
with open(input_yaml_path, 'r') as input_file:
    data = yaml.safe_load(input_file)

# Check if 'hostname' exists in the data
if 'hostname' in data.get('all', {}).get('children', {}):
    # Create a copy of the data
    modified_data = data.copy()

    # Rename the 'hostname' dictionary to 'new_hostname' in the copy
    modified_data['all']['children'][new_hostname] = modified_data['all']['children'].pop('hostname')

    # Change the hostname key within the 'new_hostname' dictionary in the copy
    modified_data['all']['children'][new_hostname]['hosts'][new_hostname] = modified_data['all']['children'][new_hostname]['hosts'].pop('hostname2')

        # Check if 'hostname2' exists in the 'hosts' dictionary
    if new_hostname in modified_data['all']['children'][new_hostname]['hosts']:
    # Update specific keys within the 'hostname2' dictionary
        modified_data['all']['children'][new_hostname]['hosts'][new_hostname]['bmc_iid'] = BMC_ID
        modified_data['all']['children'][new_hostname]['hosts'][new_hostname]['host_iid'] = Host_ID  # Use a different value if needed
        modified_data['all']['children'][new_hostname]['hosts'][new_hostname]['server_kind'] = ServerKind  # Use a different value if needed
    else:
        print("Key 'hostname2' not found in 'hosts' dictionary.")

# Check if 'vars' exists within the specific 'new_hostname' dictionary
    if 'vars' in modified_data['all']['children'][new_hostname]:
    # Update specific keys within the 'vars' dictionary
        modified_data['all']['children'][new_hostname]['vars']['bmc_prefix'] = BMC_prefix  # Define BMC_prefix
       # modified_data['all']['children'][new_hostname]['vars']['host_iid'] = host_prefix  # Define host_prefix
        modified_data['all']['children'][new_hostname]['vars']['rcp_rev'] = RCP  # Use a different value if needed
        modified_data['all']['children'][new_hostname]['vars']['host_prefix'] = host_prefix # Use a different value if needed
        modified_data['all']['children'][new_hostname]['vars']['serv_vlan'] =  server_vlan  # Use a different value if needed
        modified_data['all']['children'][new_hostname]['vars']['serv_prefix'] = serv_pre  # Use a different value if needed

    else:
        print("Key 'vars' not found in 'new_hostname' dictionary.")



    # Write the modified data to a new YAML file
    with open(output_yaml_path, 'w') as output_file:
        yaml.dump(modified_data, output_file, default_flow_style=False)

    print(f"A new OSfile file '{output_yaml_path}' created.....")
else:
    print("The 'hostname' dictionary does not exist in the original YAML file.")

input_yaml_path= lines[18]
print("ganerating inventry file....")
loadingfile()

outputfile = path + "/" +  "inventery_" + new_hostname + ".yaml"
output_yaml_path = outputfile


with open(input_yaml_path, 'r') as input_file:
    data = yaml.safe_load(input_file)

if 'all' in data and 'children' in data['all'] and 'robin_ms_pri' in data['all']['children']:
    # Check if 'sample' exists within the 'hosts' dictionary
    if 'sample' in data['all']['children']['robin_ms_pri']['hosts']:
        # Rename the 'sample' dictionary to the new variable name
        data['all']['children']['robin_ms_pri']['hosts'][new_hostname] = data['all']['children']['robin_ms_pri']['hosts'].pop('sample')
    
    if new_hostname  in data['all']['children']['robin_ms_pri']['hosts']:
        # Update the value of 'key1' for 'sample'
        data['all']['children']['robin_ms_pri']['hosts'][new_hostname]['ansible_host'] = host_ip
        data['all']['children']['robin_ms_pri']['hosts'][new_hostname]['bmc_ip'] = BMC_ip
        data['all']['children']['robin_ms_pri']['hosts'][new_hostname]['server_kind'] = ServerKind
        # Save the modified data back to the YAML file

    if 'vars' in data ['all'] :
    # Update the values of the keys within the 'vars' dictionary
        data['all']['vars']['rcidr'] = CIDR
        data['all']['vars']['rcp_ver'] = RCP
        data['all']['vars']['rnics'] = R_nics
        data['all']['vars']['rver'] = Robin_version
        data['all']['vars']['rvip'] = RVIP
        data['all']['vars']['rcp_dc_type'] = Rcpdc
    # Step 4: Save the modified content back to the duplicate file
    with open(output_yaml_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

    print(f"A new inventery file '{output_yaml_path}' has been created.....")

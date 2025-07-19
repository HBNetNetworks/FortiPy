
import fortios

fgt = fortios.FortiOS(
    base_url='https://10.82.10.254:8443',
    api_key='G7f1kHzq7nQdzzb56hnpb8HrHfzd0k',
    version=fortios.FortiOSVersion.FORTIOS_7_2,
    verify_ssl=False,
    get_global=True
)

print(fgt.serial) # Serial number of the device
print(fgt.hostname) # Hostname of the device
print(fgt.version)  # FortiOS version of the device

interfaces = fgt.interface() # Get all interfaces
interfaces = fgt.interface(name='port1') # Get specific interface by name

# print(json.dumps(fgt.system_global['results'], indent=4))

# try:
#     interfaces = fgt.interface(name='hbGuest')
#     for interface in interfaces:
#         print(f'{interface['name']} has IP {interface['ip']} and status {interface['status']}')
#         print(json.dumps(interface, indent=4))
# except:
#     print('Failed to get interface information')

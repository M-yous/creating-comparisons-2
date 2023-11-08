# Display heading
print('')
print('Devices with bad software versions')
print('----------------------------------')

# Set Variable for current version comparsion used in step 4
current_version = 'Version 5.3.1'

# Read all lines of devices information from file
file = open('devices-06.txt', 'r')
for line in file:
    # Put device info into list
    device_info_list = line.strip().split(',')
    # Put device information into dictionary for this one device
    device_info = {} # Creat the inner dictionary od device info
    device_info['name'] = device_info_list[0]
    device_info['ip'] = device_info_list[2]
    device_info['version'] = device_info_list[3]
    
    # If the version doesn't match our 'current version',
    # display a warning
    if device_info['version'] != current_version:
        print(' Device:', device_info['name'], ' Version:', device_info['version'])


checked_devices = 0
devices_to_check = ['Device1', 'Device2', 'Device3', 'Device4', 'Device5', 'Device6', 'Device7', 'Device8']
for device in devices_to_check:   
    checked_devices += 1
print('')
print(f'Number of devices cheched: {checked_devices}')


# Display  a blank line to make easier to read
print('')
# Close the file
file.close()

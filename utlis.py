import os  # Importing the os library

# Execute the 'wmic logicaldisk get size,freespace,caption' command to get disk space information
os.system('wmic logicaldisk get size,freespace,caption')

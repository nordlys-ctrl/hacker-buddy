# import libs if any

# make ascii art
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@                      @                      @                     @')
print('@                      @         @@@@@@       @                     @')
print('@                      @       @@@@@@@@@@     @                     @')
print('@                      @    @@@@@@@@@@@@@@@@  @                     @')
print('@                      @    @@@@@@@@@@@@@@@@  @                     @')
print('@                      @       @@@@@@@@@@     @                     @')
print('@                      @         @@@@@@       @                     @')
print('@                      @                      @                     @')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@                      @                      @                     @')
print('@                      @                      @        @@@@@        @')
print('@                      @                      @     @@@@@@@@@@@     @')
print('@                      @                      @   @@@@@@@@@@@@@@@   @')
print('@                      @                      @   @@@@@@@@@@@@@@@   @')
print('@                      @                      @     @@@@@@@@@@@     @')
print('@                      @                      @        @@@@@        @')
print('@                      @                      @                     @')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@                      @                      @                     @')
print('@         @@@@@        @          @@@@        @        @@@@@        @')
print('@      @@@@@@@@@@@     @       @@@@@@@@@@     @     @@@@@@@@@@@     @')
print('@    @@@@@@@@@@@@@@@   @    @@@@@@@@@@@@@@@@  @   @@@@@@@@@@@@@@@   @')
print('@    @@@@@@@@@@@@@@@   @    @@@@@@@@@@@@@@@@  @   @@@@@@@@@@@@@@@   @')
print('@      @@@@@@@@@@@     @       @@@@@@@@@@     @     @@@@@@@@@@@     @')
print('@         @@@@@        @         @@@@@@       @        @@@@@        @')
print('@                      @                      @                     @')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
# credit where credit is due
print('hacker-buddy v.0.0.1 alpha')
print('')
print(' "I Knew You Were Trouble" ')
print('')
print('created by nordlys-ctrl')
print('')
proceedInput = input("first time setup?[y/n] \n")
print('')
# note to me and who it might concern, start with simple commands, making 4 files to save passwords, macs
# associations, and ips, and create an association eg: file Mac_Storage line 13:   Jimmy John = xx:xx:xx:xx:xx;
# same with ips and passwords fName lName = info
# make separate files for mac address, ip, associations and passwords
# association file should be connecting real name to internet alias or tag
# eventually make an option to encrypt whatever is being put in but not decrypt need like JtR or something
if proceedInput == 'y':
    print('running first time setup')
    macFile = open("mac_storage.txt", "w+")
    macFile.close()
    ipFile = open("ip_storage.txt", "w+")
    ipFile.close()
    passFile = open("pass_storage.txt",  "w+")
    passFile.close()
    connectFile = open("connect_storage.txt", "w+")
    connectFile.close()
    print('')
    print('setup complete 4 files created')
    print('')
    print('IMPORTANT')
    print('TO FINISH FIRST TIME SETUP TYPE --b OR --break')
    print('THEN RE-RUN hacker-buddy')
    print('')

print('')
print('proceeding to hacker-buddy')
print('')
iMac = 0
iIp = 0
iPass = 0
iConn = 0
while True:
    usrInput = input('enter command \n')
    print('')

    if usrInput == '--help' or usrInput == '--h':
        print('help command recognised')
        print('')
        print('hacker-buddy v.0.0.1 alpha')
        print('')
        print('--h or --help: see this list of commands')
        print('--b or --break: break loop, done command')
        print('')
        print('--mac: command to log mac address')
        print('--ip: command to log ip address')
        print('--pass: command to log password')
        print('--conn: command to connect aliases')
        print('')
        print('--mac --read: command to read all macs in file')
        print('--ip --read: command to read all ips in file')
        print('--pass --read: command to read all passwords')
        print('--conn --read: command to read all connections made in file')
        print('')
        print('')

    elif usrInput == '--break' or usrInput == '--b':
        print('exiting hacker-buddy')
        break

    elif usrInput == '--mac':
        print('mac address command detected')
        print('')
        macName = input('what is the name/alias of the victim? \n')
        print('')
        macFile = open("mac_storage.txt", "a+")
        macAddress = input('what is the mac address? \n')
        macFile.write(macName + " = " + macAddress + "\r\n")

    elif usrInput == '--ip':
        print('ip address command detected')
        print('')
        ipName = input('what is the name/alias of the victim? \n')
        print('')
        ipFile = open("ip_storage.txt", "a+")
        ipAddress = input('what is the ip address? \n')
        ipFile.write(ipName + " = " + ipAddress + "\r\n")

    elif usrInput == '--pass':
        print('password command detected')
        print('')
        passName = input('what is the name/alias of the victim? \n')
        print('')
        passFile = open("pass_storage.txt", "a+")
        password = input('what is the password? \n')
        passFile.write(passName + " = " + password + "\r\n")

    elif usrInput == '--conn':
        print('connect command detected')
        print('')
        print('you will need to type all connections you know eg: "__xX__Xx__ = Johnny Bravo"')
        print('')
        connectFile = open("connect_storage.txt", "a+")
        connectString = input('type out all connections\n')
        connectFile.write(connectString + "\r\n")

    elif usrInput == '--mac --read':
        print('read mac command detected')
        print('')
        macFile = open("mac_storage.txt", "r")
        for x in macFile:
            print(x)

    elif usrInput == '--ip --read':
        print('read ip command detected')
        print('')
        ipFile = open("ip_storage.txt", "r")
        for x in ipFile:
            print(x)

    elif usrInput == '--pass --read':
        print('read password command detected')
        print('')
        passFile = open("pass_storage.txt", "r")
        for x in passFile:
            print(x)

    elif usrInput == '--conn --read':
        print('read connect command detected')
        print('')
        connectFile = open("connect_storage.txt", "r")
        for x in connectFile:
            print(x)

    else:
        print('command not recognised, press --h or --help for a list')

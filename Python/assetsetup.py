import os
import MySQLdb
import subprocess
import os
import shutil
from subprocess import STDOUT, check_call
##Author: Rezkon
## When your lazy and you like something..script it!.

print "Installing SQL Stuff.."


##requirements()
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def requirements():
    try:
        print bcolors.OKBLUE + "Setting up Stuff.."
        subprocess.check_call("apt-get update", shell=True)
        subprocess.check_call("apt-get install mysql-server", shell=True)
        subprocess.check_call("apt-get install python-dev, python-bcrypt, libmysqlclient-dev", shell=True)
        subprocess.check_call("sudo mysql_secure_installation", shell=True)
        subprocess.check_call("sudo mysql_install_db", shell=True)
    except subprocess.errno:
        print "Something happened...not sure what..UM..run?"


print "setting up......"
requirements()
print "Creatin a database..."
password = raw_input(bcolors.WARNING +"Do you have a password set for your sql, if so please enter it?, if not leave blank\n" + bcolors.ENDC)

db1 = MySQLdb.connect(host="localhost", user="root", passwd=password)
cursor = db1.cursor()
sql = 'create DATABASE testing'
cursor.execute(sql)
print "Database Created...\n"
print bcolors.FAIL + "Doing some horrible hacking stuff...\n" + bcolors.ENDC
PUSHKEY = raw_input(bcolors.WARNING + "Please enter your pushover application's key.\n")
config = open("config.py").read()
config = config.replace('testing', password)
config = config.replace('PUSHNOTIFYKEY', PUSHKEY)
connote = open('config.py', 'w')
connote.write(config)
connote.close()

email = "Please enter a username..\n"
asset = open("assetnote.py").read()
asset = asset.replace('shubs', email)
note = open('assetnote.py', 'w')
note.write(asset)
note.close()

subprocess.check_call("apt-get install python-pip", shell=True)
print "Pip requirements."
subprocess.check_call("pip install -r requirements.txt", shell=True)


print "Please move config.py to managers folder..\n"
print bcolors.FAIL + bcolors.BOLD + "PLEASE CHANGE THE REQUIRED THINGS IN THE CONFIG.PY FILE\n" + bcolors.ENDC
print bcolors.FAIL + bcolors.UNDERLINE + "Thankyou to Shubs @infosec_au and @nnwakelam for assetnote"

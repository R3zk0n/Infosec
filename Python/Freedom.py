import os
import frida
import requests
import subprocess
import os
import zipfile

# Probs should ensure that the applesign binary is done..#

def Check_Deps():
	print "Checking Dependacy's"
	# if null return error. 
	# if not null return true. 
	os.exec("applesign")
	print

def Frida_Download():
    print "Installing Frida..\n"
    try:
        from frida import __version__ as FRIDA_VERSION
    except ImportError:
        print()


def AppleSign():
    entitlements = subprocess.check_output(['applesign', '-L'])
    print "First Entitlement: %s" % entitlements.split(" ")[0]

    IPAPackage = raw_input("Please enter full path to the IPA file \n")
    iOSSign = file(IPAPackage)
    iOSUnzip_zip = zipfile.ZipFile(iOSSign)
    iOSUnzip_zip.extractall(iOSSign)
    iOSUnzip_zip.close()
    # This should sign the application.
    signing = subprocess.check_output(
        ['applesign', '-i', "%s", ""]), entitlements.split(" ")[0]




if __name__ == '__main__':

    AppleSign()

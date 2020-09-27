#!/usr/bin/python3

'''
This is Class for ycn agent libvirt operations

Author : Dhanasekara Pandian
Email  : sekar5in@quehive.com, dhana.s@contecuae.com
CopyRights : All Rights are Reserved
'''

#Global Import
import pprint
import sys
import libvirt


class DomainManage:

    def __init__(self):
        try:
            self.conn = libvirt.open('qemu:///system')
            if self.conn == None:
                print('Failed to open connection to qemu:///system', file=sys.stderr)
                exit(1)
        except Exception as e:
            print(e)
            exit(255)

    def isalive(self):
        alive = self.conn.isAlive()
        return alive

    def get_hostname(self):
        hostName = self.conn.getHostname()
        return hostName
    
    def get_issecure(self):
        isSecure = self.conn.isSecure()
        return isSecure

    def get_version(self):
        ver = self.conn.getVersion()
        return ver

    def get_sysinfo(self):
        '''
        Returns XML info of System
        Parameters:
        return : xmlinfo
        '''
        xmlInfo = self.conn.getSysinfo()
        return xmlInfo

    def close(self):
        self.conn.close()
        exit(0)



# Boiler Plate 
if __name__ == "__main__":
    
    #Initialize Object
    obj = DomainManage()
    alive_status = obj.isalive()
    print("Connection is alive = " + str(alive_status))

    if alive_status == 1:

        #Get the version of Qemu
        ver = obj.get_version()
        print('Version: '+str(ver))

        #Get the sysinfo of Qemu
        xmlinfo = obj.get_sysinfo()
        print(xmlinfo)

        #Close the Connection
        obj.close()

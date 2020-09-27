#!/usr/bin/python3

'''
This is Class for ycn agent libvirt Guest operations

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

    def listdomain(self):
        domainIDs = self.conn.listDomainsID()
        if domainIDs == None:
            print('Failed to get a list of domain IDs', file=sys.stderr)
        
        print("Active domain IDs:")
        if len(domainIDs) == 0:
            print('  None')
        else:
            for domainID in domainIDs:
                print('  '+str(domainID))

    def close(self):
        self.conn.close()
        exit(0)



# Boiler Plate 
if __name__ == "__main__":
    
    #Initialize Object
    obj = DomainManage()

    # List domains
    obj.listdomain()

    #Close the Connection
    obj.close()

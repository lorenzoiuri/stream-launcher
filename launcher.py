import xml.etree.ElementTree as ET
import sys
from subprocess import call

def printUsage():
    usageStr = "usage: "
    usageStr += str(sys.argv[0])
    usageStr += " id"
    print(usageStr)
    
def printLibrary(root):
    initialMessage = "";
    initialMessage += "Found "
    initialMessage += str(len(root)) 
    initialMessage += " elements in library"
    print(initialMessage)
    for i in range(0,len(root)):
        msg = " | "
        msg += root[i][0].text
        msg += " (id = "
        msg += root[i][1].text
        msg += ")"
        print(msg)

tree = ET.parse('library.xml')
root = tree.getroot()

if (len(sys.argv) != 2):
    printUsage()
    printLibrary(root)
    sys.exit(1)
    
#now i need to get the url from the id

for i in range(0,len(root)):
    if (root[i][1].text == sys.argv[1]):
        call(["mpv", root[i][2].text])
        
    







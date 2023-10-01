import requests
import sys
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

inputargsn = sys.argv

logging.basicConfig(filename="std.log", format='%(asctime)s %(levelname)s %(message)s', filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG) 

def getdata_dneonline(newurl, newfname):
    try:
        #url = "http://www.dneonline.com/calculator.asmx"
        #f = open("addHelper.xml", "rt")
        f = open(newfname, "rt")
        payload = f.read()  
        f.close()
        headers = {
            'Content-Type': 'text/xml'
        }
        response = requests.request("POST", newurl, headers=headers, data=payload)
        logger.debug(response.text)
        print(response.text)
    except Exception as e:
        print("Err: ", e)


def addHelpercall():
    getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
    logger.info("============================================================")
    print("============================================================")

def subHelpercall():
    getdata_dneonline("http://www.dneonline.com/calculator.asmx", "subHelper.xml")
    logger.info("============================================================")
    print("============================================================")

def temperatureHelperCall():
    getdata_dneonline("https://www.w3schools.com/xml/tempconvert.asmx", "temperatureHelper.xml")
    logger.info("============================================================")
    print("============================================================")

def noteHelpercall():
    getdata_dneonline("https://www.dataaccess.com/webservicesserver/NumberConversion.wso", "noteHelper.xml")

def allinone():
    addHelpercall()
    subHelpercall()
    temperatureHelperCall()
    noteHelpercall()


def switchAppAPIs(n):
    if n == 'AD':
        addHelpercall()
    elif n == 'SB':
        subHelpercall()
    elif n == 'TP':
        temperatureHelperCall()
    elif n == 'A':
        noteHelpercall()
    else:
        allinone()

for n in inputargsn[1:]:
    switchAppAPIs(n)
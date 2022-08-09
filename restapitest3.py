import requests
import logging

logging.basicConfig(filename="std.log", format='%(asctime)s %(levelname)s %(message)s', filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG) 

def getdata_dneonline(newurl, newfname):
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

getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
logger.info("============================================================")
getdata_dneonline("http://www.dneonline.com/calculator.asmx", "subHelper.xml")  
logger.info("============================================================")
getdata_dneonline("https://www.w3schools.com/xml/tempconvert.asmx", "temperatureHelper.xml")
logger.info("============================================================")
getdata_dneonline("https://www.dataaccess.com/webservicesserver/NumberConversion.wso", "noteHelper.xml")

import requests


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
    print(response.text)

getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
print("============================================================")
getdata_dneonline("http://www.dneonline.com/calculator.asmx", "subHelper.xml")  
print("============================================================")
getdata_dneonline("https://www.w3schools.com/xml/tempconvert.asmx", "temperatureHelper.xml")
print("============================================================")
getdata_dneonline("https://www.dataaccess.com/webservicesserver/NumberConversion.wso", "noteHelper.xml")
import requests


def getdata_dneonline(newurl, newfname,x,y):
    #url = "http://www.dneonline.com/calculator.asmx"
    #f = open("addHelper.xml", "rt")
    f = open(newfname, "rt")
    payload = f.read()  
    f.close()
    headers = {
        'Content-Type': 'text/xml'
    }
    response = requests.request("POST", newurl, headers=headers, data=payload.format(a=x,b=y))
    print(response.text)

print("============================================================")
getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelpers.xml",3,4)
print("============================================================")
getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelpers.xml",5,14)
print("============================================================")
getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelpers.xml",15,14)
print("============================================================")
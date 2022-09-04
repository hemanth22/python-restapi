import requests
import logging
from typing import Optional
from typing import Union
from fastapi import FastAPI, Response

#from enum import Enum


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(filename="std.log", format='%(asctime)s %(levelname)s %(message)s', filemode='w')

logger=logging.getLogger()

logger.setLevel(logging.DEBUG) 

def getdata_dneonline(newurl, newfname,x,y):
    try:
        #url = "http://www.dneonline.com/calculator.asmx"
        #f = open("addHelper.xml", "rt")
        f = open(newfname, "rt")
        payload = f.read()  
        f.close()
        headers = {
            'Content-Type': 'text/xml'
        }
        response = requests.request("POST", newurl, headers=headers, data=payload.format(a=x,b=y))
        logger.debug(response.text)
        return response.text
    except Exception as e:
        print("Err: ", e)


#untangle.parse(getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml"))

app = FastAPI()

@app.get('/addition')
async def calculator_add(inputA: int, inputB: int):
    #return getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
    return Response(content=getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelpers.xml",inputA,inputB), media_type="application/xml")

@app.get('/subtraction')
async def calculator_sub(inputA: int, inputB: int):
    #return getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
    return Response(content=getdata_dneonline("http://www.dneonline.com/calculator.asmx", "subHelpers.xml",inputA,inputB), media_type="application/xml")

@app.get('/Multiply')
async def calculator_multiply(inputA: int, inputB: int):
    #return getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
    return Response(content=getdata_dneonline("http://www.dneonline.com/calculator.asmx", "multipleHelpers.xml",inputA,inputB), media_type="application/xml")

@app.get('/Division')
async def calculator_divide(inputA: int, inputB: int):
    #return getdata_dneonline("http://www.dneonline.com/calculator.asmx", "addHelper.xml")
    return Response(content=getdata_dneonline("http://www.dneonline.com/calculator.asmx", "divideHelpers.xml",inputA,inputB), media_type="application/xml")

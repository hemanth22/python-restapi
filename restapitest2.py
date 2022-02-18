import xml.etree.ElementTree as ET
import requests

url = "http://www.dneonline.com/calculator.asmx"

payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\r\n<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\r\n  <soap:Body>\r\n    <Add xmlns=\"http://tempuri.org/\">\r\n      <intA>3</intA>\r\n      <intB>4</intB>\r\n    </Add>\r\n  </soap:Body>\r\n</soap:Envelope>"
headers = {
  'Content-Type': 'text/xml'
}

response = requests.request("POST", url, headers=headers, data=payload)

tree = ET.fromstring(response.text)

for xmlresponse in tree.findall('.//{*}AddResult'):
    print('Connection: {0} , price: {1} '.format(response.status_code,xmlresponse.text))
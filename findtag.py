import xml.etree.ElementTree as ET

tree = ET.parse('calc.xml')
root = tree.getroot()
#print(ET.tostring(root))

print("=== Before namespaces finding")

for xmlresponse in tree.findall('.//'):
    print(xmlresponse)

print("=== After namespaces finding")
for xmlresponse in tree.findall('.//{http://tempuri.org/}AddResult'):
    print(xmlresponse.text)

for xmlresponse in tree.findall('.//{*}AddResult'):
    print(xmlresponse.text)

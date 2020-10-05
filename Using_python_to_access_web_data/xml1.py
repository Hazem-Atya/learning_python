import xml.etree.ElementTree as ET

data = ''' <person>  
<name>Hazem</name>
<phone type="intl">
+21625969655
</phone>
<email hide="yes"/>
</person>'''
# ''' for multilines strings
tree = ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

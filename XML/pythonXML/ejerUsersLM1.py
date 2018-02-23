from lxml import etree
doc = etree.parse('users.xml')

usuarios = doc.findall ("user")
for usuario in usuarios:
    print (usuario[0].text)
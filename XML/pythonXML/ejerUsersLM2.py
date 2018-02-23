from lxml import etree
doc = etree.parse('users.xml')
usuarios = doc.findall ("user")
for usuario in usuarios:
	foto = usuario.find("picture")
	if foto.text == "1":
		print (usuario[0].text)

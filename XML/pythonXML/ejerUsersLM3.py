from lxml import etree
doc = etree.parse('users.xml')
usuarios = doc.findall ("user")
for usuario in usuarios:
	if usuario.findtext("lastip").startswith ("172.22") != usuario.find("lastip"):
		print (usuario.findtext ("email"))

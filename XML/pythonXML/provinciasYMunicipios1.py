from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

raiz = doc.getroot ()

# 1) Programa que lista todas las provincias.
for x in range (len(raiz)):
	provincia = raiz [x]
	print (provincia[0].text)
localidad = doc.findall ("provincia/nombre")
for x in range localidad:
	print (x.text)
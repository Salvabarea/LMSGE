from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

raiz = doc.getroot ()

#2) Programa que lista todos los municipios.
for x in range (len(raiz)):
	provincia = raiz [x]
	print (provincia[0].text)
	for i in range (len(provincia[1])):
		print (provincia[1][i].text)
# Otra versión:
localidad = doc.findall ("provincia/localidades/localidad")
for x in localidad:
	print (x.text)

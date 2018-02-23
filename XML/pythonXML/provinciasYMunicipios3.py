from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

raiz = doc.getroot ()

#3) Programa que muestra la lista de provincias y el total de municipios que tiene cada una.
for x in range (len(raiz)):
	provincia = raiz [x]
	print ("Provincia:",provincia[0].text)
	print ("Número de municipios:",len(provincia[1]))
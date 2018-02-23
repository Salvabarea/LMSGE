from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

#6) En una lista tenemos distintos identificadores de provincias, mostrar el nombre de las provincias y
# todos los municipios correspondientes a los identificadores que se encuentran en la lista.
listaIdProvincias = ['01', '33', '13']
provincias = doc.findall('provincia')
for provincia in provincias:
	if provincia.attrib['id'] in listaIdProvincias:
		print ("Provincia: ", provincia[0].text)
		localidades=provincia[1].findall("localidad")
		for localidad in localidades:
			print (localidad.text)
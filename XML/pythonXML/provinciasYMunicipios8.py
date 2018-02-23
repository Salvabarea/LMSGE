from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

#8) Programa que lea una localidad y te diga si es "ciudad grande" 
#atributo c="1") o no de provincia. Si es "ciudad grande" 
#de provincia te muestra su nombre.
poblacion = input ("Dime la poblacion: ")
provincias = doc.findall("provincias")
for provincia in provincias:
	localidades = provincia[1].findall("localidad")
	if localidad in localidades:
		if localidad.text == poblacion:
			if localidades.attrib['c'] == '1':
				print (poblacion,"es una ciudad grande de",provincia[0].text)
			else:
				print(poblacion,"no es una ciudad grande")
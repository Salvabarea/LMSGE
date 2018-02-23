from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')

#4) Programa que lea por teclado el nombre de una provincia y muestra sus municipios.
provincias = doc.findall("provincia")
prov_nombre = input("Introduce el nombre de la provincia: ")
for provincia in provincias:
    nombre = provincia.find('nombre')
    if nombre.text == prov_nombre:
        localidades = provincia.findall('localidades/localidad')
        for localidad in localidades:
            print (localidad.text)
import xml.etree.ElementTree as ET
import re


def nuevaNota(f, h, p):
    # crea la estructura del archivo
    notas = ET.Element('notas')
    nota = ET.SubElement(notas, 'nota')
    fecha = ET.SubElement(nota, 'fecha')
    hora = ET.SubElement(nota, 'hora')
    parrafo = ET.SubElement(nota, 'p')

    fecha.text = f
    hora.text = h
    parrafo.text = p

    # Inserta una nueva línea en el xml con el resutado
    mynota = ET.tostring(notas)
    file = open("notas.xml", "a")
    notaFinal = re.sub(r'.', '', str(mynota), 2)
    file.write(notaFinal[:-1])


def imprimir_notas():
    tree = ET.parse('notas.xml')
    root = tree.getroot()

    for elem in root:
        for subelem in elem:
            print(subelem.text)
        print("")


print("Bienvenido a tu aplicación de gestión de notas: \n"
      "-Si quiere imprimir todas sus notas escriba: imprimir\n"
      "-Si quiere insertar una nueva nota escriba: insertar")
entrada = input()
if entrada == 'imprimir':
    imprimir_notas()
if entrada=="insertar":
    print("Escriba los datos a insertar separados por espacios en el siguiente orden: fecha, hora y contenido de la "
          "nota")
    string=input()
    lista=string.split(" ")
    nuevaNota(lista[0], lista[1], lista[2])


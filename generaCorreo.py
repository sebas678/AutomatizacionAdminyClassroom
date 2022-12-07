from tkinter import filedialog as fd #Libreria para escoger archivo
import xlrd

vocEspe="áäéëíïóöúüñÁÄÉËÍÏÓÖÚÜÑ"
vocTrans="aaeeiioouunAAEEIIOOUUN"

def correoLote(path):
    try:
        dataUsuario=xlrd.open_workbook(path)
        hojaData=dataUsuario.sheet_by_index(0)
        try:
            columnas=hojaData.nrows
            print(columnas)
            for i in range (1, columnas):
                nombress=(str(hojaData.cell_value(i,0)))
                apellidoss=(str(hojaData.cell_value(i,1)))
                correoIndiv(nombress, apellidoss)
        except:
            print("Error en las columnas de información")
    except:
        print("Error en la dirección o tipo de dato")

def correoIndiv(nombres,apellidos):
    correo=""

    nombreIndiv = nombres.split()
    for nombre in nombreIndiv:
        correo=correo+nombre[0]

    apellidoSep=apellidos.split()

    if len(apellidoSep) < 4:
        if(apellidoSep[0].lower()=="de" or apellidoSep[0].lower=="del" or apellidoSep[0].lower=="dela" ):
            apellido=apellidoSep[0]+apellidoSep[1]
        else:
            print("Correo debe crearse a mano")

        correo=correo+"."+apellido
        correo=correo.lower()
        trans=correo.maketrans(vocEspe,vocTrans)
        mail=correo.translate(trans)

        print(mail)
    else:
        print("Correo debe ser creado a mano")    


def main():
    opcion = int(input("""
    1. Crear correo individual
    2. Crear correos desde archivo

    Ingrese un numero: """))
    if opcion == 1:
        nombress=input("Ingrese nombres  ")
        apellidoss=input("Ingrese apellidos  ")
        correoIndiv(nombress,apellidoss)
        
    elif opcion==2:
        ruta = fd.askopenfilename()#abre explorador de archivos para elegir ruta
        print(ruta)
        correoLote(ruta)
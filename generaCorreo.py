vocEspe="áäéëíïóöúüñÁÄÉËÍÏÓÖÚÜÑ"
vocTrans="aaeeiioouunAAEEIIOOUUN"

nombres=input("Ingrese nombres  ")
apellidos=input("Ingrese apellidos  ")

correo=""

nombreIndiv = nombres.split()
for nombre in nombreIndiv:
    correo=correo+nombre[0]

apellidoSep=apellidos.split()

if len(apellidoSep) < 4:
    if(apellidoSep[0].lower()=="de" or apellidoSep[0].lower=="del" or apellidoSep[0].lower=="dela" ):
        apellido=apellidoSep[0]+apellidoSep[1]

correo=correo+"."+apellido
correo=correo.lower()
trans=correo.maketrans(vocEspe,vocTrans)
mail=correo.translate(trans)

print(mail)
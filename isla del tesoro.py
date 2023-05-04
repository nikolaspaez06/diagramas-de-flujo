print("bienbenidos a la isla del tesoro,tu mision es encontrar el tesoro ")
print("derecha,izquierda:")
#elegir = Input().strip().lower()
elegir = str(input("Pon aqui tu opcion: ")).strip().lower()
if elegir == "derecha":
    print("caisteen un agujero")
    print("fin")
    quit()
elif elegir == "izquierda":
    print("pasar")
    print("esperar")
else:
    print("fin")

detener = str(input("pon aqui tu opcion:")).strip().lower()
if  detener == "pasar":
    print("atacado por una tribu")
    print("fin")
    quit()
elif  detener == "esperar":
    print("una persona te enseña unas puertas")
    print("pueta verde")
    print("puerta azul")
else:
    print("fin")
escoger = str(input("pon aqui tu opcion:")).strip().lower()
if escoger == "puerta verde":
    print("azul") 
    print("devorado por bestias")
    print("fin")
elif escoger == "puerta azul":
    print("encontraste el tesoro")
    print("HAS GANADO")










    






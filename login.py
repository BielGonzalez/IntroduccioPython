usuari = "Biel"
contraseña = "smx"
usuari_preguntat = str(input("Quin es el teu usuari? "))
contraseña_preguntada = str(input("Quina es la teva contraseña? "))
if usuari == usuari_preguntat and contraseña == contraseña_preguntada:
	print("Inici de sessio correcte")
else:
	print("Hi ha hagut un error de autenticacio")

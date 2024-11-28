import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)

    return res

def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    if jugada_usuario == jugada_ordenador:
        return "Empate"
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijeras":
        return "Ganaste"
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        return "Ganaste"
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        return "Ganaste"
    else:
        return "Perdiste"
    
def jugar():
    print("Bienvenido")
    ord = ordenador_decide_jugada()
    usu = usuario_decide_jugada()
    print("La elección del ordenador es: ", ord)
    res = determina_ganador(usu, ord)
    print(res)
    return res

def jugar_torneo():
    puntos_jugador = 0
    puntos_maq = 0
    while puntos_jugador < 3 and puntos_maq < 3:
        res = jugar()
        if res == "Ganaste":
            puntos_jugador += 1
        elif res == "Perdiste":
            puntos_maq += 1
    if (puntos_maq >= 3):
        print("Ha ganado la maquina")
    elif (puntos_jugador >= 3):
        print("Ha ganado el jugador")
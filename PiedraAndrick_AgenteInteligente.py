import random
def irrigation_System():

    costo_agua = 0
    '''Estados iniciales del suelo y de la humedad del suelo'''
     
    print("Humedad del Suelo = 1-Bajo, 2-Medio, 3-Alto")
    print("Estado del Suelo = 0-Seco, 1-Humedo")
    
    '''Humedad del Suelo: 0 - Bajo, 1 - Medio, 2 - Alto'''
    humedad_suelo = int(input("Ingresar Nivel de Humedad del suelo: "))
    
    '''Estados Posibles de la humedad de suelo'''
    suelo_humedad={'bajo':3, 'medio':2,'alto':1}

irrigation_System()
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

    '''Estados Posibles del suelo'''
    suelo_estados={'seco':0,'humedo':1}
    
    '''Estados globales inicializados en 0, para posteriormente agregar valores randoms'''
    estado_global = {'Parcela_1': 0 , 'Parcela_2': 0,'Parcela_3': 0,
                     'Parcela_4': 0 , 'Parcela_5': 0,'Parcela_6': 0,
                     'Parcela_7': 0
                     }
    for llave, valor in estado_global.items():
        estado_global[llave]= random.randint(0, 1)

    '''Bucle for que permie comprobar primeramente el estado de la humedad del suelo,
    
        luego se crea otro bucle que recorre los estados globales comprobando el estado del suelo'''
    
    for llave_humedad, value_humedad in suelo_humedad.items():
        try:
            if humedad_suelo == value_humedad:
                print("Humedad del suelo "+str(llave_humedad))
                print("Estado Global:" + str(estado_global))
                for llave_estado, value_estado in estado_global.items():
                        if value_estado ==1:
                          print(str(llave_estado)+" con tierra humeda")
                        #si la habitacion se encuentra en estado 1(fria) entonces
                        if value_estado==0:
                          #Habitacion esta fria
                          print(str(llave_estado)+" con tierra seca. Regando Parcela! ")
                          estado_global[llave_estado] = 1
                          costo_agua = costo_agua+1 * humedad_suelo
        except:
            print("Ingrese valor entre 0 y 1")

irrigation_System()
import random
import time
import pyttsx3

cartas_pasadas = []
cartas_loteria = [
'El gallo', ' El diablito' , ' La dama', ' El catrín' , ' El paraguas' , ' La sirena' , ' La escalera', 
' La botella' , ' El barril', ' El árbol' , ' El melón', ' El valiente', ' El gorrito', ' La muerte'
, ' La pera', ' La bandera', ' El bandolón', ' El violoncello', ' La garza', ' El pájaro', ' La mano'
, ' La bota', ' La luna', ' El cotorro', ' El borracho', ' El negrito', ' El corazón', ' La sandía'
, ' El tambor', ' El camarón', ' Las jaras', ' El músico', ' La araña', ' El soldado', ' La estrella'
, ' El cazo', ' El mundo', ' El apache', ' El nopal', ' El alacrán', ' La rosa', ' La calavera'
, ' La campana', ' El cantarito', 'El venado', 'El sol', 'La corona', ' La chalupa', 'El pino'
, ' El pescado', ' La palma', ' La maceta', ' El arpa', 'La rana']


def Jugar():
    for i in range(54):
        time.sleep(1)
        engine = pyttsx3.init()
        carta_loteria = random.choice(cartas_loteria)
        if carta_loteria not in cartas_pasadas:
            cartas_pasadas.append(carta_loteria)
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            engine.say(carta_loteria)
            print(carta_loteria)
        else:
            Jugar()
        engine.runAndWait()
        
            
Jugar()
import csv
from time import sleep
import pyautogui as p
import pyperclip as pc
# puede ser necesario instalar pillow - cmd: pip install pillow

dir = "ListaTusArchivos-Script-v4 - Musica.csv"


                                                                 
'''7MN.   `7MF'        mm                    `YMM'   `MM'MMP""MM""YMM 
    MMN.    M          MM                      VMA   ,V  P'   MM   `7 
    M YMb   M        mmMMmm   ,pW"Wq.           VMA ,V        MM      
    M  `MN. M          MM    6W'   `Wb           VMMP         MM      
    M   `MM.M  mmmmm   MM    8M     M8 mmmmm      MM          MM      
    M     YMM          MM    YA.   ,A9            MM          MM      
  .JML.    YM          `Mbmo  `Ybmd9'           .JMML.      .JMML      1.0'''    
                                                                    



def listarCanciones(dir : str) -> dict:
    #Path Completo,Carpeta,Archivos,Nombre Archivo,Fecha,Tamaño MB,URL,ID,Descripción,Tipo archivo,Cambiar Descripcion,Resultado
    with open(dir, 'r', encoding="UTF8") as archivo:
        archivo_canon = csv.reader(archivo)
        novos = {}

        # diccionario
        for linea in archivo_canon:
            # verificar/agregar carpeta
            novo_actual = linea[1]
            if novo_actual not in novos.keys():
                novos[novo_actual] = []
            
            # filtrar nombre de canción
            cancion = linea[3].replace('.mp3', '').replace('(MP3_160K)','').replace('(MP3_128K)','').replace('(MP3_320K)','')

            # si no es un audio, si el título no es nulo y si la canción no está repetida en la misma carpeta
            if cancion[0:3] != 'AUD' and cancion not in ['',' ','  ','­','­ ­'] and ((cancion[-2:] != '_1' and cancion[-3:] != '(1)') or novo_actual in ['-Novo 5-','-Novo 6-']):
                # agregar canción
                cancion_filtrada = cancion if cancion[-2:] != '_1' else cancion[:-2]
                novos[novo_actual].append(cancion_filtrada)

    return novos

def buscar() -> None:
    try:
        buscar_texto()
    except:
        try:
            buscar_x()
        except:
            buscar_bar()
            p.write('backspace')


# True : Stop | False : Continue
def exception_confirmar(ex : str) -> bool:
    try:
        p.locateCenterOnScreen(f'images/Exception_{ex}.PNG', confidence=0.9)
        return True
    except:
        return False #safe
    
def pegar() -> None:
    p.keyDown('ctrl')
    p.press('v')
    p.keyUp('ctrl')


def sussy_baka(lista : list) -> None:
    for cancion in lista:
        print(cancion)
    print(f'\n[ {len(lista)} canciones en total ]')

    sleep(5)
    opera()

    stop = 0
    for num in range(len(lista)):
        print(f'{num}/{len(lista)} | {round(((num+1)/len(lista)) *100 , 2)}% | {lista[num]}')

        #write
        buscar()
        #p.write(lista[num], 0.05)
        pc.copy(lista[num])
        pegar()

        lupa()
        sleep(2)

        #exceptions
        if exception_confirmar('para_ti'): continue
        ex = exception_confirmar('mal_escrito')
        x = 880 if exception_confirmar('album') else 1306

        #add
        try:
            points_up(x)
            menu_cola(1, x)
        except:
            try:
                points(x, ex)
                menu_cola(2, x, ex)
            except:
                points_down(x)
                menu_cola(3, x)

        sleep(0.5)

        #stop each 10
        if stop == 10:
            #cola
            sleep(2)
            p.press('i')
            sleep(6)
            p.press('i')
            sleep(6)

            #terminal
            stop = 0
            visual()
            terminal()
            sleep(5)
            opera()
        stop +=1
    p.press('i')
    visual()
    terminal()
        



# --------------- miau -------------------

def pos(): p.displayMousePosition()

def cerrar():       p.click(1344, 15, duration=0.2)

def cola():         p.click(606, 263, duration=0.2)

def terminal():     p.moveTo(p.locateCenterOnScreen('images/Terminal.PNG', confidence=0.9), duration=0.1)

def opera():        p.click(p.locateCenterOnScreen('images/Opera.PNG', confidence=0.9), duration=0.2)

def visual():       p.click(p.locateCenterOnScreen('images/Visual.PNG', confidence=0.9), duration=0.2)

def buscar_texto(): p.click(p.locateCenterOnScreen('images/Buscar.PNG', confidence=0.9), duration=0.2)

def buscar_x():     p.click(p.locateCenterOnScreen('images/Buscar_x.PNG', confidence=0.9), duration=0.2)

def buscar_bar():   p.click(630, 125, duration=0.2)

def lupa():         p.click(p.locateCenterOnScreen('images/Lupa.PNG', confidence=0.9), duration=0.2)

#  --------------- fuck you -------------------

def menu_cola(level : int = 2, x : int = 1306, ex : bool = False):    
    try:
        sleep(0.7)
        p.click(p.locateCenterOnScreen('images/Menu_cola.PNG', confidence=0.8), duration=0.3)
    except:
        if level == 1: points_up(x)
        if level == 2: points(x, ex)
        if level == 3: points_down(x)
        sleep(0.5)
        p.click(p.locateCenterOnScreen('images/Menu_cola_icon.PNG', confidence=0.9), duration=0.4)

def points_up(x = 1306):    p.click(x+4, 204, duration=0.3)

def points(x = 1306, ex=False): 
    if ex:  p.click(x, 295, duration=0.3)
    else:   p.click(x, 237, duration=0.3)

def points_down(x = 1306):  p.click(x, 304, duration=0.3)


# ------------ thx novvae ----------------

if __name__ == '__main__':
    novos = listarCanciones(dir)
    #novos = {'-Rock-': ['La costa del silencio','Bruno Mars - Locked out of haven','Gorillaz - Feel Good Inc.','System Of A Down - Toxicity', 'back in black', 'Red Hot Chili Peppers - Scar Tissue [Official Music Video]']}

    while True:
        print('\n¿Qué lista quisieras?', list(novos.keys()), '-> ', sep='\n', end='')

        # escoger la lista de reproducción/carpeta a crear en yt
        lista_actual = input()
        if lista_actual == '0': break
        if lista_actual.isnumeric():     lista_actual = f'-Novo {lista_actual}-'
        if lista_actual[0] != '-':       lista_actual = f'-{lista_actual}-'
        print(lista_actual)
        
        when = 'Está en la lista, hora del sexo' if lista_actual in novos.keys() else 'Eres un imbécil'
        print(when, '\n')

        if when != 'Eres un imbécil': sussy_baka(novos[lista_actual])

    print('La re buena, chao')
    #print(novos)  son todas las canciones

# para ver las canciones que no fueron buscadas según los filtros
'''
for i in novos:
    for j in novos[i]:
        if j[0:3] == 'AUD' or (j[-2:] == '_1' and i not in ['-Novo 5-','-Novo 6-']):
            print(j)
'''

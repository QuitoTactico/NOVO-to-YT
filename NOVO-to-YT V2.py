import csv
from time import sleep
import pyautogui as p
import pyperclip as pc

# puede ser necesario instalar pillow - cmd: pip install pillow

dir = "NOVO/INPUT/ListaTusArchivos-Script-v4 - Musica.csv"


"""7MN.   `7MF'        mm                    `YMM'   `MM'MMP""MM""YMM 
    MMN.    M          MM                      VMA   ,V  P'   MM   `7 
    M YMb   M        mmMMmm   ,pW"Wq.           VMA ,V        MM      
    M  `MN. M          MM    6W'   `Wb           VMMP         MM      
    M   `MM.M  mmmmm   MM    8M     M8 mmmmm      MM          MM      
    M     YMM          MM    YA.   ,A9            MM          MM      
  .JML.    YM          `Mbmo  `Ybmd9'           .JMML.      .JMML   2.9.2"""


def listarCanciones(dir: str) -> dict:
    # Path Completo,Carpeta,Archivos,Nombre Archivo,Fecha,Tamaño MB,URL,ID,Descripción,Tipo archivo,Cambiar Descripcion,Resultado
    with open(dir, "r", encoding="UTF8") as archivo:
        archivo_canon = csv.reader(archivo)
        novos = {}

        # diccionario
        for linea in archivo_canon:
            # verificar/agregar carpeta
            novo_actual = linea[1]
            if novo_actual not in novos.keys():
                novos[novo_actual] = []

            # filtrar nombre de canción
            cancion = (
                linea[3]
                .replace(".mp3", "")
                .replace("(MP3_160K)", "")
                .replace("(MP3_128K)", "")
                .replace("(MP3_320K)", "")
            )

            # si no es un audio, si el título no es nulo y si la canción no está repetida en la misma carpeta
            if (
                cancion[0:3] != "AUD"
                and cancion not in ["", " ", "  ", "­", "­ ­"]
                and (
                    (cancion[-2:] != "_1" and cancion[-3:] != "(1)")
                    or novo_actual in ["-Novo 5-", "-Novo 6-"]
                )
            ):
                # agregar canción
                cancion_filtrada = cancion if cancion[-2:] != "_1" else cancion[:-2]
                novos[novo_actual].append(cancion_filtrada)

    return novos


def sussy_baka(lista: list, carpeta: str) -> None:
    for cancion in lista:
        print(cancion)
    print(f"\n[ {len(lista)} canciones en total ]")

    sleep(5)
    imagen_click("Opera")
    stop = 0
    excepciones = 0
    excepciones_lista = []

    for num in range(len(lista)):
        stop += 1
        print(
            f"{num+1}/{len(lista)} | {round(((num+1)/len(lista)) *100 , 2)}% | {lista[num]}"
        )

        buscar_cancion(lista, num)

        if imagen_buscar("Exception_para_ti"):
            excepciones += 1
            excepciones_lista.append({"numero": num, "nombre": lista[num]})
            continue

        try:
            agregar_cancion(carpeta)
        except:
            excepciones += 1
            excepciones_lista.append({"numero": num, "nombre": lista[num]})

        # stop each 10
        if stop == 10:
            stop = 0
            revisar_cola()
            revisar_terminal()

    p.press("i")
    imagen_click("Visual")
    terminal()
    print(f"Excepciones: {excepciones}")
    for i in excepciones_lista:
        print(f"{i['numero']}\t| {i['nombre']}")


def agregar_cancion(carpeta):
    ver_puntos()
    try:
        sleep(2)
        imagen_click("Points", minSearchTime=0.5)
    except:
        sleep(0.5)
        revisar_terminal()
        sleep(2)
        ver_puntos()
        sleep(2)
        try:
            imagen_click("Points", region=None, minSearchTime=2)
        except:
            return None
    finally:
        try:
            sleep(1)
            imagen_click("Agregar_a_lista")
        except:
            sleep(2)
            imagen_click("Agregar_a_lista")
        finally:
            try:
                sleep(1.5)
                imagen_click(f"Novo/{carpeta}", confidence=0.99)
            except:
                sleep(2)
                imagen_click(f"Novo/{carpeta}", confidence=0.97)
            finally:
                p.press("esc")

    """
    try:
        sleep(0.7)
        imagen_click('Menu_cola')
    except:
        sleep(1)
        imagen_click('Menu_cola_icon')
    """


def buscar_cancion(lista, num):
    buscar()
    pc.copy(lista[num])
    pegar()
    imagen_click("Lupa")
    sleep(2)


def buscar() -> None:
    try:
        imagen_click("Buscar")
    except:
        try:
            imagen_click("Buscar_x")
        except:
            barra_busqueda()
            p.write("backspace")


def pegar() -> None:
    p.keyDown("ctrl")
    p.press("v")
    p.keyUp("ctrl")


def revisar_terminal():
    imagen_click("Visual")
    terminal()
    sleep(5)
    imagen_click("Opera")


def revisar_cola():
    sleep(2)
    p.press("i")
    sleep(6)
    p.press("i")
    sleep(6)


def ver_puntos():
    p.moveTo(670, 325, 0.5)


def terminal():
    p.moveTo(690, 625, 0.2)


def barra_busqueda():
    p.click(630, 125, duration=0.2)


# ----------- image functions ------------


# True : Existe | False : No papu :'V
def imagen_buscar(image: str) -> bool:
    try:
        p.locateCenterOnScreen(f"NOVO/images/{image}.PNG", confidence=0.9)
        return True
    except:
        return False  # safe en casos de excepciones


def imagen_mover(image, confidence=0.8, duration=0.2):
    p.moveTo(
        p.locateCenterOnScreen(f"NOVO/images/{image}.PNG", confidence=confidence),
        duration=duration,
    )


def imagen_click(image, confidence=0.8, duration=0.2, region=None, minSearchTime=None):
    try:
        p.click(
            p.locateCenterOnScreen(
                f"NOVO/images/{image}.PNG",
                confidence=confidence,
                region=region,
                minSearchTime=minSearchTime,
            ),
            duration=duration,
        )
    except:
        p.click(
            p.locateCenterOnScreen(
                f"NOVO/images/{image}.PNG",
                confidence=0.75,
                region=region,
                minSearchTime=2,
            ),
            duration=duration,
        )


# ------------ ejecución ----------------


def pos():
    p.displayMousePosition()


# pos()

lista_de_prueba = {
    "-Prueba-": [
        "La costa del silencio",
        "Bruno Mars - Locked out of haven",
        "Gorillaz - Feel Good Inc.",
        "System Of A Down - Toxicity",
        "Portugues",
        "back in black",
        "Red Hot Chili Peppers - Scar Tissue [Official Music Video]",
        "[MV] 이달의 소녀_츄 (LOONA_Chuu) _Heart Attack_",
    ]
}


def escoger(novos):
    while True:
        print("\n¿Qué lista quisieras?", list(novos.keys()), "-> ", sep="\n", end="")

        # escoger la lista de reproducción/carpeta a crear en yt
        carpeta = input()
        if carpeta == "0":
            break
        if carpeta.isnumeric():
            carpeta = f"-Novo {carpeta}-"
        if carpeta[0] != "-":
            carpeta = f"-{carpeta}-"
        print(carpeta)

        when = (
            "Está en la lista, hora del sexo"
            if carpeta in novos.keys()
            else "Eres un imbécil"
        )
        print(when, "\n")

        if when != "Eres un imbécil":
            desde = int(input("Desde dónde bro? -> "))
            lista = novos[carpeta][desde:]
            sussy_baka(lista, carpeta)


def preseleccionadas(novos):
    elegidos = ["-Novo 1-", "-Novo 2-", "-OP - EN-", "-Electro-"]

    for carpeta in elegidos:
        lista = novos[carpeta]
        sussy_baka(lista, carpeta)


if __name__ == "__main__":
    novos = listarCanciones(dir)
    # novos = lista_de_prueba

    opcion = input("1. Escoger\n2. Preseleccionadas\n-> ")
    if opcion == "1":
        escoger(novos)
    elif opcion == "2":
        preseleccionadas(novos)

    print("La re buena, chao")

import datetime

#-------------------------------------------------#
#             Funktionsdefinitionen               #
#                     log()                       #
#-------------------------------------------------#

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

def getfiletext(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Die Datei unter dem Pfad {file_path} wurde nicht gefunden.")
    except IOError as e:
        raise IOError(f"Ein Fehler beim Lesen der Datei ist aufgetreten: {e}")
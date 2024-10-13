import argparse
import platform,os
from pathlib import Path
import string,random

sys = platform.system()
actual_user = os.getlogin()

def compute_default_path(OS = platform.system(),user = os.getlogin()):
    if OS == "Windows":
        target_folder = os.path.realpath("C:/Users/"+user+"/Documents")
    # TODO : UNIX Porting
    return target_folder

parser = argparse.ArgumentParser(description="Ransomware dans tes morts",formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-e","-encrypt","--encrypt", action="store_true",help="Encryption Mode", default=None)
parser.add_argument("-d","-decrypt","--decrypt", action="store_true",help="Decryption Mode",default =None )
parser.add_argument("-k","-key", "--key", help="Encryption / Decryption Key", default=None)
parser.add_argument("--path","-path","-p", help="Répertoire Cible, par défaut sur windows ",default=compute_default_path())
parser.add_argument("--demo","-demo",action="store_true" ,help="Mode de démonstration",default=False)
parser.add_argument("--keyLength","-keyLength",help="Si clé de chifrement non précisé, précise la taille de la clé à générer",default=25)
parser.add_argument("-v","-verbose","--verbose",action="store_true",help="Active l'affichage des actions en temps réel", default = False)
# TODO : Add provoque feature (html page to avert from the attack)

args = parser.parse_args()
config = vars(args)

def genRandomKey(length):
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

def encrypt(key):
    #TODO
    pass

def decrypt(key):
    #TODO
    pass

def main():
    global config
    # STEP 0 = SET TARGET PATH
    target = compute_default_path()
    if config['path']!=compute_default_path():
        target= os.path.realpath(config['path'])    
    # NOT STEP - VERBOSE MODE
    if config['verbose']:
        print("Mode verbose activé\n Emplacement cible de l'attaque -->"+target)

    # ENCRYPT_MODE
    if config['encrypt']:
        #TODO STEP 1
        pass
    #DECRYPT_MODE
    if config['decrypt']:
        #TODO STEP 1
        pass
    return


main()
#print(genRandomKey(config['elength']))
#print(car)
#print(config['path'])
#print(actual_user)
#print(type(sys))
#print(config)
# Return {'encrypt': None, 'decrypt': None, 'key': None, 'path': 'C:\\\\Users\\\\Administrator\\\\Documents', 'demo': 'C:\\\\Users\\\\Administrator\\\\Documents', 'keyLength': 25, 'verbose': False}
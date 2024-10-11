# MyRans0mware

## ⚠️ Disclaimer ⚠️

Ce projet est créé à des fins de formations sur les méthodes utilisés par les hackeurs pour le chiffrement des données. L'objectif, à travers ce code est de montrer les meilleurs façons pour s'en prémunir et s'en protéger.

L'utilisation de ce projet a des fins malveillantes peut entraîner des poursuites judiciaires et des sanctions pénales à la hauteur du dommage causé.

## ✅ Compatibilité ✅

Uniquement fonctionnel avec les systèmes d'exploration Windows pour le moment. (Portage systèmes UNIX à venir)

## ❓ Help ❓

Options de l'algo de ransomware

### -p, -path, --path : Argumment pour définir l'emplacement cible

##### Par défaut : 

**Windows** : C:\Users\{username}\Documents\
**Linux** : /home/{username}/ **ou** /var/www/html/ (In Progress)

### -e, -encrypt, --encrypt

Mode de chiffrement des données, si aucune clé n'est spécifiée, clé générée aléatoirement

⚠️Données sans connaissance de la clé de chiffrement = données irrécupérables ⚠️

### -d, -decrypt, --decrypt

Mode de déchiffrement des données, clé de chiffrement **obligatoire**

### -k, -key, --key

Argument de commmande &larr; Spécifie la clé de chiffrement

### --demo, -demo

Activation du mode de démonstration

#### Spécificités du mode démonstration

(TODO)

### --keyLength, -keyLength

Si aucune clé de chiffrement n'est spécifiée, permets de spécifier la taille d'une clé de chiffrement

### -v, --verbose, -verbose

Active l'affichage des actions en temps réel

(TODO : ADD FEATURES)

## Documentation de la CNIL au sujet des attaques de types rançongiciel (ou ransomware)

[> Vers la documentation de la CNIL](https://www.cnil.fr/fr/cybersecurite/multiplication-des-attaques-par-rancongiciel-comment-limiter-les-risques)
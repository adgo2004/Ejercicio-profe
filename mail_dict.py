#definim en una variable de tipus dict, la clau serà el nom i el valor serà el email
#posem els noms i els correus electrònics de la classe
diccionari = {
        "Mercedes": "mcast386@xtec.cat",
        "Rayane": "rayane@rayane.sa",
        "Mohamed": "moha@gmail.com",
        "Jad": "jad@gmail.com",
        "Oriol": "joam@gmail.com",
        "Elias": "hola123@gmail.com",
        "Armau": "arnau@gmail.com",
        "Asdrúbal": "asdrubal@gmail.com",
        "Adrian": "pedrosanchez@asix2.com",
        "Emma": "pacosanz@gmail.com",
        "Nishwan": "nishwan@gmail.com",
        "Javi": "javi@gmail.com",
        "Novel": "novelferreras49@gmail.com",
        "Bruno": "elcigala@gmail.com",
        "David": "argentino@gmail.com",
        "Judit": "judit@gmail.com",
        "Joao": "joao@gmail.com",
        "Laura": "laura@gmail.com",
        "Enrico": "123@gmail.com",
        "Joel": "joelcobre@gmail.com",
        "Aaron": "aaron@gmail.com",
        "Moad": "moad@gmail.com",
        }

#CONSTANTS pel resultat de les fucions
NOTROBAT = "NOTROBAT"
AFEGIT = "AFEGIT"
MODIFICAT = "MODIFICAT"
JAEXISTEIX = "JAEXISTEIX"

# funció getmaildict rep el nom com paràmetre i retorna el mail
# si no el troba retorna un string "NOTROBAT"
def getmaildict(nom):
      if nom in diccionari:
         return diccionari[nom]
      return NOTROBAT

# addmaildict rep el nom i el email com paràmetres, i els afegeix al diccionari
# si ja existeix retorna un string "JAEXISTEIX"
# quan va bé retorna string "AFEGIT"
# si el paràmetre modif es True, quan ja existeix però és diferent, el modifica i retorna string "MODIFICAT"
def addmaildict(nom,correu,modif=False):
      oldcorreu = getmaildict(nom)
      if oldcorreu == NOTROBAT:
        diccionari[nom]=correu
        return AFEGIT
      elif (oldcorreu != correu and modif):
        diccionari[nom]=correu
        return MODIFICAT
      return JAEXISTEIX
   
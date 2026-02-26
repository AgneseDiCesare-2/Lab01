import random

gioca=True
levelTarget=0
maxLevel=0
punti=0

class Domanda:

    def __init__(self, testo: str, livello: int, corretta: str, errata1: str, errata2: str, errata3:str):
        self.__testo = testo
        self.__livello = livello
        self.__corretta = corretta
        self.__errata1 = errata1
        self.__errata2 = errata2
        self.__errata3 = errata3

    def risposte(self):
        risposte=[self.corretta, self.errata1, self.errata2, self.errata3]
        random.shuffle(risposte)
        return risposte

    @property
    def testo(self):
        return self.__testo

    @property
    def livello(self):
        return self.__livello
    @property
    def corretta(self):
        return self.__corretta

    @property
    def errata1(self):
        return self.__errata1

    @property
    def errata2(self):
        return self.__errata2

    @property
    def errata3(self):
        return self.__errata3

    def __str__(self):
        return f"testo: {self.__testo} \n opzioni: {self.risposte()}"

    #metto un setter di livello così controllo i valori
    @livello.setter
    def livello(self, livello):
        if livello < 0 or livello > 10:
            print("livello non corretto")
        self.__livello = livello

with open("domande.txt", "r", encoding="utf-8") as f:
    file=f.readlines()
    domande=[]

    #divido il file in range di 7 righe e salvo le domande come oggetti
    for i in range (0, len(file), 7):
        temp=Domanda(file[i].strip(), int(file [i+1].strip()), file[i+2].strip(), file[i+3].strip(), file[i+4].strip(), file[i+5].strip())
        domande.append(temp)
    for domanda in domande:
        if domanda.livello > maxLevel:
            maxLevel=domanda.livello

def seleziona():
    selezionate = []
    for domanda in domande:
        if (domanda.livello == levelTarget):
            selezionate.append(domanda)
    return selezionate

while (gioca):
    seleziona()
    domandaScelta = random.choice(seleziona()) #NB
    opzioni = domandaScelta.risposte()
    print(domandaScelta)
    risposta=str(input("scrivi la risposta: "))
    #rispostaStringa=domandaScelta.risposte()[risposta] #prendo il numero corrispondente dall'array di risposte

    if (risposta != domandaScelta.corretta):
        gioca=False
        print("risposta errata")

    if (domandaScelta.livello==maxLevel and risposta==domandaScelta.corretta):
        gioca=False
        punti=punti+1
        print("complimenti, hai finito il gioco!")

    else:
        levelTarget=levelTarget+1
        punti=punti+1

#quando esce dal gioco
print(f"Congratulazioni, hai ottenuto il punteggio di: {str(punti)}")
nickname=str(input("inserisci il tuo nickname: "))

#salvo i dati nel file
with open ("punti.txt", "a", encoding="utf-8") as inputFile:
    inputFile.write(f"{nickname} {punti}\n") #aggiungi il punteggio

with open("punti.txt", "r", encoding="utf-8") as iFile: #leggi il file completo
    file=iFile.readlines()
    giocatori=[]
    dizionario={}

    for riga in file:
        dati=riga.strip().split(" ") #array di tipo giocatore, punteggio
        nome=dati[0]
        punteggio=dati[1]
        giocatori.append(nome) #se mi assicuro che il nickname sia univoco posso creare un dizionario
        dizionario[nome]=int(punteggio)#tipo nickname:punteggio

ordinati = sorted(dizionario.items(), key=lambda x: x[1], reverse=True) #STRUTTURA PER ORDINARE

with open("punti.txt", "w", encoding="utf-8") as outputFile: #sovrascrivi il file ordinato
    for nome, punteggio in ordinati:
        outputFile.write(f"{nome} {punteggio}\n")

#se usassi "a" al posto di "w" non cancellerei il file, ma aggiungerei le informazioni



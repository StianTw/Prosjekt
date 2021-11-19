# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:09:43 2021

@author: stw34
"""

class sporsmaal:
    
    def __init__(self, svar, spm, riktigsvar):
      self.svar = svar
      self.spm= spm
      self.riktigsvar= riktigsvar
    
    def __str__(self):
      resultat = f"{self.spm}\n"
      for svaralternativer in self.svar:
          resultat += svaralternativer + "\n"
      return resultat
  
    def sjekksvar(self, brukersvar):
        return int(brukersvar) == self.riktigsvar
            
    def korrekt_svar_tekst(self):
        return self.svar[self.riktigsvar]

class Spiller:

    def __init__(self, navn):
        self.navn = navn
        self.poengsum = 0
        
        
    
def load():
    sporsmaallist= []
    with open("sporsmaalsfil.txt", "r", encoding = "UTF8") as fila:
        for linje in fila:
            ordene = linje.split(":")
            spm = ordene[0]
            rettsvar = int(ordene[1].strip())
            svar = [s.strip() for s in ordene[2].strip()[1:-1].split(",")]
            
            sporsmaallist.append(sporsmaal(svar, spm, rettsvar))
            
    return sporsmaallist

def last_spillere():
    spillerliste= []
    antallspillere = int(input("Skriv inn antall spillere: "))
    for i in range(0, antallspillere):
        spillerliste.append(Spiller(input("Skriv inn navn på spiller {}: ".format(i+1))))
       
    return spillerliste             




if __name__ == "__main__":

    sporsmaalliste = load()
    spillerliste = last_spillere()
    
    for spm in sporsmaalliste:
        print()
        print(spm.spm)
        print("Svaraltarnativer:")
        for i, svaralternativ in enumerate(spm.svar):
            print("{}. {}".format(i, svaralternativ))
        svar = []   
        for spiller in spillerliste:
            svar.append(input("Velg et svar alternativ for spiller {}: ".format(spiller.navn)))
        print ()
        print ("Korrekt svar: {}".format(spm.korrekt_svar_tekst()))
        print ()
        for i, spiller in enumerate(spillerliste):
            if spm.sjekksvar(svar[i]):
                print ("Spiller {}: Korrekt".format(spiller.navn))
                spiller.poengsum += 1
            else:
                print ("Spiller {}: Feil".format(spiller.navn))
    
    vinner = spillerliste[0]
    print()
    print("Resultat!")
    for spiller in spillerliste:
        print()
        print("Spiller {} Poengsum: {}".format(spiller.navn, spiller.poengsum))
        if spiller.poengsum > vinner.poengsum:
            vinner = spiller
    print()
    print("Vinneren med høyest poengsum er {} med {} poeng.".format(vinner.navn, vinner.poengsum))
     
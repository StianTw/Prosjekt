# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:34:13 2021

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
  
    def sjekksvar(self, bruker):
        if bruker == self.riktigsvar:
            return "Du valgte riktig svar"
        else:
            return "Du har valgt feil svar"

    def korrekt_svar_tekst(self):
        return self.svar[self.riktigsvar]
    
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


if __name__ == "__main__":
    Spiller1score = 0
    Spiller2score = 0
    sporsmaalliste = load()
    
    for spm in sporsmaalliste:
        print(spm.spm)
        print("Svaraltarnativer:")
        for i, svaralternativ in enumerate(spm.svar):
            print("{}. {}".format(i, svaralternativ))
            
        Spiller1svar = input("Velg et svaralternativ for spiller 1: ")
        Spiller2svar = input("Velg et svaralternativ for spiller 2: ")
        print ("Korrekt svar: {}".format(spm.korrekt_svar_tekst()))  
        
        Spiller1korrektsvar = "Korrekt" if int(Spiller1svar) == spm.riktigsvar else "Feil"
        print ("Spiller 1: {}".format(Spiller1korrektsvar))
        
        if Spiller1korrektsvar == "Korrekt":
            Spiller1score += 1
        
        Spiller2korrektsvar = "Korrekt" if int(Spiller2svar) == spm.riktigsvar else "Feil"
        print ("Spiller 2: {}".format(Spiller2korrektsvar))
        
        if Spiller2korrektsvar == "Korrekt":
            Spiller2score += 1
            
    print("Total score:")
    print("Spiller 1 score: {}".format(Spiller1score))
    print("Spiller 2 score: {}".format(Spiller2score))
            
            
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 16:34:13 2021

@author: stw34
"""





class spill:
    
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

s1=spill(["k2", "himalaya", "preikestolen"],"Hva er det hoyeste fjellet", 1)
print(s1)
brukerinputt= int(input("Velg alternativ"))
print (s1.sjekksvar(brukerinputt))

s2=spill(["1992","1993","1998"], "Nor ble hurtigruten 100år", 1)
print(s2)
brukerinputt= int(input("Velg alternativ"))
print (s2.sjekksvar(brukerinputt))
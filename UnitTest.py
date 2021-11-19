# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 19:16:38 2021

@author: stw34
"""

import unittest

from ProsjektPythonØving9del2 import sporsmaal 

class SporsmaalTest(unittest.TestCase):
    def setUp(self):
        svar = ["RAM", "Harddisk", "CPU", "Sekundærlager"]
        self.spm = sporsmaal(svar, "Den delen av en datamaskin som kjører programmet kalles?", 2)

    def test_sjekksvar(self):
        self.assertTrue(self.spm.sjekksvar("2"))
        self.assertFalse(self.spm.sjekksvar("3"))
    
    def test_korrekt_svar_tekst(self):
        self.assertEqual(self.spm.korrekt_svar_tekst(), "CPU")
        self.assertNotEqual(self.spm.korrekt_svar_tekst(), "RAM")
         
if __name__ == '__main__':
    unittest.main()
    
    
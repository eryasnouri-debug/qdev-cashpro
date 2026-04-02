import unittest
from cashpro.reduction import calculerReduction

class calculerReductionUnitTest(unittest.TestCase):
    def test_calculerReduction(self):
        #cas 1: montant 15, fidélité Vrai -> 0%
        self.assertEqual(calculerReduction(15.0, True), 0)     
        #Cas 2: Montant 32, fidélité Vrai -> 5%
        self.assertEqual(calculerReduction(32.0, True), 5)  
        #Cas 3: Montant 100, fidélité Vrai -> 10%
        self.assertEqual(calculerReduction(100.0, True), 10)   
        #cas 4: Montant 201, fidélité Vrai -> 15%
        self.assertEqual(calculerReduction(201.0, True), 15)    
        #Cas 5: Montant 200, fidélité Faux -> 0%
        self.assertEqual(calculerReduction(200.0, False), 0) 
        #cas 6: Montant 50, fidélité Faux -> 0%
        self.assertEqual(calculerReduction(50.0, False), 0)  
        #Cas 7: Montant -10, fidélité vrai -> error (ValueError)
        with self.assertRaises(ValueError): 
            calculerReduction(-10.0, True) 

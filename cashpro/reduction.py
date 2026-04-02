def calculerReduction(montant_total, est_fidele):
    if montant_total < 0:
        raise ValueError("Le montant total ne peut pas être inférieur à 0,00 €") 
    if not est_fidele:
        return 0
    # Barème pour les clients adhérents 
    if montant_total >= 200.0:
        return 15 
    elif montant_total >= 100.0:
        return 10
    elif montant_total >= 30.0:
        return 5 
    else:
        return 0 

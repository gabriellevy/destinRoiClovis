init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from despin.reglages import filtres_action
    from humanite import trait
    from univers import temps
    from humanite.sante import pbsante

    estChetif = condition.Condition(trait.Constitution.NOM, trait.Trait.SEUIL_A_PAS_EXTREME, condition.Condition.INFERIEUR_EGAL)
    estFragile = condition.Condition(trait.Constitution.NOM, trait.Trait.SEUIL_A_PAS, condition.Condition.INFERIEUR_EGAL)
    estResistant = condition.Condition(trait.Constitution.NOM, trait.Trait.SEUIL_A, condition.Condition.SUPERIEUR_EGAL)
    estIndestructible = condition.Condition(trait.Constitution.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.SUPERIEUR_EGAL)
    def AjouterEvtsMaladies():
        global selecteur_
        probaMaladie = proba.Proba(0.01)
        probaMaladie.ajouterModifProbaViaVals(0.01, estFragile)
        probaMaladie.ajouterModifProbaViaVals(0.01, estChetif)
        probaMaladie.ajouterModifProbaViaVals(-0.005, estResistant)
        probaMaladie.ajouterModifProbaViaVals(-0.005, estIndestructible)

        decTombeMalade = declencheur.Declencheur(probaMaladie, "decTombeMalade")
        selecteur_.ajouterDeclencheur(decTombeMalade)

label decTombeMalade:
    $ maladie = maladies_.TomberMaladeAleatoirement(situation_)
    $ texteMaladie = maladie.GetDescriptionRecu()
    "[texteMaladie]"

    jump fin_cycle

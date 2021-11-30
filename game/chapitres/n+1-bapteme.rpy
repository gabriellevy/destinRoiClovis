init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import pnj
    from abs.humanite import metier
    from abs.univers import temps
    from abs.humanite import identite
    from chapitres.classes import germains
    from chapitres.classes import clovis

    auMoinsAnnee497 = condition.Condition(temps.Date.DATE_ANNEES, 497, condition.Condition.SUPERIEUR_EGAL)
    enDecembre = condition.Condition(temps.Date.MOIS_ACTUEL, 12, condition.Condition.EGAL)
    foiSupCinq = condition.Condition(clovis.Clovis.C_CHRISTIANISME, 5, condition.Condition.SUPERIEUR) # considéré (pour l'instant) comme foi suffisante pour le baptème

    # événements liés à la conversion de Clovis puis à son baptème
    def AjouterEvtBapteme():
        global selecteur_
        bapteme = declencheur.Declencheur(proba.Proba(1.0, False), "bapteme") # événement obligatoire en décembre
        bapteme.AjouterCondition(auMoinsAnnee497)
        bapteme.AjouterCondition(enDecembre)
        bapteme.AjouterCondition(foiSupCinq)
        selecteur_.ajouterDeclencheur(bapteme)

label bapteme:
    scene bg bapteme
    "Ainsi, à Reims dans la nuit de Noël 497, Saint-Rémi baptisa Clovis avec 3 000 de ses soldats."
    "Les populations gallo-romaines accueillirent les Francs non plus comme des envahisseurs mais comme des libérateurs."
    "L'Église, qui était la plus haute autorité spirituelle, choisit ainsi le camp des Francs."
    jump appel_divin

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

    auMoinsAnnee492 = condition.Condition(temps.Date.DATE_ANNEES, 492, condition.Condition.SUPERIEUR_EGAL)
    # conditions clotilde
    infos_sur_clotildePasFaite = condition.Condition("infos_sur_clotilde", 1, condition.Condition.DIFFERENT)

    def AjouterEvtsClothilde():
        global selecteur_
        infos_sur_clotilde = declencheur.Declencheur(proba.Proba(0.7, True), "infos_sur_clotilde")
        infos_sur_clotilde.AjouterCondition(auMoinsAnnee496)
        selecteur_.ajouterDeclencheur(infos_sur_clotilde)

label infos_sur_clotilde:
    scene bg tolbiac
    # play music guerre2 noloop
    $ situation_.SetValCarac("infos_sur_clotilde", 1)
    show clotilde at right
    with dissolve
    clot "A FAIRE Coucou Clovis !"
    jump fin_cycle

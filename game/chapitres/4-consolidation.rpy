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
    from chapitres.classes import syagrius
    from chapitres.classes import clovis

    auMoinsAnnee490 = condition.Condition(temps.Date.DATE_ANNEES, 490, condition.Condition.SUPERIEUR_EGAL)
    guerre_burgonde490PasFaite = condition.Condition("guerre_burgonde490", 1, condition.Condition.DIFFERENT)

    def AjouterEvtBurgondes():
        global selecteur_
        guerre_burgonde490 = declencheur.Declencheur(proba.Proba(0.9, True), "guerre_burgonde490")
        guerre_burgonde490.AjouterCondition(auMoinsAnnee490)
        guerre_burgonde490.AjouterCondition(guerre_burgonde490PasFaite)
        selecteur_.ajouterDeclencheur(guerre_burgonde490)

label guerre_burgonde490:
    play music guerre1 noloop
    $ situation_.SetValCarac("guerre_burgonde490", 1)

    "PAS FAIT : première guerre burgonde"
    jump fin_cycle

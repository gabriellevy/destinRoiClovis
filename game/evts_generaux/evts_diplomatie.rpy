init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from chapitres.classes import clovis
    from spe import dec_clo

    diplomatieSup0 = condition.Condition(clovis.Clovis.C_DIPLOMATIE, 0, condition.Condition.SUPERIEUR)
    def AjouterEvtsDiplomatie():
        global selecteur_
        mariage_aldoflede = dec_clo.DecClovisU(proba.Proba(0.2, True), "mariage_aldoflede", 483)
        mariage_aldoflede.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(mariage_aldoflede)
        # joueur de citharède
        citharede = dec_clo.DecClovisU(proba.Proba(0.08, True), "citharede", 483)
        citharede.AjouterCondition(estRoi)
        citharede.AjouterCondition(diplomatieSup0)
        selecteur_.ajouterDeclencheur(citharede)

label citharede:
    scene bg citharede
    "Théodoric vous a envoyé comme présent un joueur de citharède, un instrument à corde très rare en Gaule."
    "Voilà qui égayera vos repas et réceptions, et augmentera le prestige de votre cour."
    $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
    jump fin_cycle

label mariage_aldoflede:
    "Théodoric, grand roi des Ostrogoths d'Italie, demande la main de votre soeur Aldoflède."
    "C'est un très bon parti car il est non seulement puissant en lui-même mais en bon termes avec l'empire romain d'Orient."
    menu:
        "En tant que chef de famille c'est à vous d'accepter ou de refuser."
        "Accepter":
            "Aldoflède se convertit au christianisme arien comme son époux puis elle part en Italie pour le rejoindre."
            "Ces bons rapports avec le plus grand souverain germain renforcent nettement votre réputation et votre influence."
            $ AjouterACarac(clovis.Clovis.C_DIPLOMATIE, 1)
        "Refuser":
            "Théodoric se considérant comme le plus important des souverains germains il prend mal votre refus. Et son influence est telle que vos relations avec les autres royaumes sont affaiblies aussi."
            $ RetirerACarac(clovis.Clovis.C_DIPLOMATIE, 1)

    jump fin_cycle

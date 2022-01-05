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

    def AjouterEvtsDiplomatie():
        global selecteur_
        mariage_aldoflede = dec_clo.DecClovisU(proba.Proba(0.2, True), "mariage_aldoflede", 483)
        mariage_aldoflede.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(mariage_aldoflede)

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

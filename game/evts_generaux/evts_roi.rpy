init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from chapitres.classes import clovis

    def AjouterEvtsRoi():
        global selecteur_
        # remplacement de comte
        comtCritique = declencheur.Declencheur(proba.Proba(0.03, True), "comtCritique")
        comtCritique.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(comtCritique)
        # nommage de comte
        nommageComte = declencheur.Declencheur(proba.Proba(0.02, True), "nommageComte")
        nommageComte.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(nommageComte)

label comtCritique:
    $ nomComte = francs_.CreerPrenom(True)
    "Le comte [nomComte] à votre service se comporte paraît-til comme un brigand. Il vole et frappe ses sujets et les plaintes s'accumulent."
    "Il est par contre d'une fidélité à toute épreuve envers vous et fait rentrer les impôts très efficacement."
    menu:
        "Le réprimander publiquement":
            "Les galloromains apprécident de voir que leurs demandes sont entendues. Le comte [nomComte] n'ose plus les pressurer autant qu'avant."
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
            jump fin_cycle

        "Le faire exécuter":
            "Le peuple est satisfait de voir son tourmenteur mort, mais les autres comtes sont terrifiés de voir que la fidélité envers vous ne leur garantit pas votre clémence."
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
            jump fin_cycle

        "le laisser agir à sa guise tant que les impôts entrent":
            "Le peuple est écrasé mais l'argent coule à flot."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
            jump fin_cycle

        "le remplacer discrètement":
            "Les galloromains apprécident de voir que leurs demandes sont entendues."
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
            jump nommageComte
    jump fin_cycle


label nommageComte:
    "PAS FAIT : nommageComte"
jump fin_cycle

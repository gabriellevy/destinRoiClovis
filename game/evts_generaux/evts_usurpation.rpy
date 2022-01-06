init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from chapitres.classes import clovis

    # si l'usurpation et à plus de 0 il y a risque de soulèvement contre Clovis
    ilYARisqueDUsurpation = condition.Condition(clovis.Clovis.C_USURPATION, 0, condition.Condition.SUPERIEUR)
    def AjouterEvtsUsurpation():
        global selecteur_
        usurpation = declencheur.Declencheur(proba.Proba(0.07, True), "usurpation")
        usurpation.AjouterCondition(ilYARisqueDUsurpation)
        usurpation.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(usurpation)

label usurpation:
    play music danger noloop
    # des nobles tentent de prendre le pouvoir du roi
    $ niveauUsurpation = situation_.GetValCaracInt("niveauUsurpation")
    # plus la gloire est élevée plus il y a de chances de surmonter l'usurpation
    $ test = testDeCarac.TestDeCarac(clovis.Clovis.C_GLOIRE, niveauUsurpation, situation_)
    $ reussi = test.TesterDifficulte(situation_)
    menu:
        "TMP attention usurpation"
        "Chances de réussite : [test.affichage_]":
            pass
    if reussi:
        # usurpation évitée
        jump fin_cycle
    else:
        if niveauUsurpation == 0:
            $ situation_.SetValCarac("niveauUsurpation", 1)
            "Vos guerriers, surtout l'aristocratie, apprécient peu votre attitude. Dans votre dos on vous traite de traître aux coutumes franques et de lâche."
            "Vous parvenez à garder le contrôle par un mélange de répression et de corruption et ils en restent aux grognements."
            "Mais que ce soit par la gloire ou la purge des indésirables, il va vous falloir relever votre autorité."
            jump fin_cycle
        elif niveauUsurpation == 1:
            $ situation_.SetValCarac("niveauUsurpation", 2)
            "Cela faisait longtemps que le mécontentement couvait mais cette fois vos guerriers sont furieux contre vous."
            "Plusieurs tentent de vous atteindre pour vous agresser mais sont repoussés par vos fidèles. La rixe dégénère vite et plusieurs francs sont tués dans chaque camps."
            "Les assaillants se replient mais il est hors de question de laisser passer un tel acte, vous donnez immédiatement les ordres pour les éliminer ainsi que leur famille."
            "La répression dure deux jours et deux nuits durant lesquels les rebelles sont massacrés et les neutres ramenés à l'obéissance par la terreur."
            "La veille du troisième jour vous avez retrouvé votre autorité mais le prix a payé a été énorme."
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 2)
            $ RetirerACarac(trait.Richesse.NOM, 2)
            $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 2)
            $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
        elif niveauUsurpation == 2:
            $ situation_.SetValCarac("niveauUsurpation", 3)
            $ usurpateur = francs_.CreerPrenom(True)
            "Vous êtes réveillé en pleine nuit par des bruits de combats."
            "Vous sautez hors de votre lit pour décrocher votre francisque mais à peine retourné vers la porte l'arme à la main dix guerriers en armes ont déjà pénétré dans votre chambre."
            "Ils sont menés par le prince [usurpateur], votre pire ennemi dans la nobless franque."
            "Votre résistance est digne de votre rang mais vouée à l'échec contre des guerriers d'élite en armure."
            "[usurpateur] attend que vous voyiez suffisament affaibli et vous fracasse le crâne d'un coup de hache. votre corps est encore chaud que vos propres guerriers pillent votre chambre et terrifient Clothilde."
            "Gloire à [usurpateur] le nouveau roi."
            jump mort

    jump fin_cycle

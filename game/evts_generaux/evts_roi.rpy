init -5 python:
    import random
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import modifProba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier
    from chapitres.classes import clovis

    fideliteGauleMoinsQue0 = condition.Condition(clovis.Clovis.C_FIDELITE_GAULE, 0, condition.Condition.INFERIEUR)
    fideliteGauleMoinsQue2 = condition.Condition(clovis.Clovis.C_FIDELITE_GAULE, 2, condition.Condition.INFERIEUR)
    fideliteGaulePlusQue0 = condition.Condition(clovis.Clovis.C_FIDELITE_GAULE, 0, condition.Condition.SUPERIEUR)
    fideliteGaulePlusQue2 = condition.Condition(clovis.Clovis.C_FIDELITE_GAULE, 2, condition.Condition.SUPERIEUR)
    fideliteGaulePlusQue3 = condition.Condition(clovis.Clovis.C_FIDELITE_GAULE, 3, condition.Condition.SUPERIEUR)
    richessePlusQue0 = condition.Condition(trait.Richesse.NOM, 0, condition.Condition.SUPERIEUR)
    armeeMoinsQue2 = condition.Condition(clovis.Clovis.C_MILITAIRE, 2, condition.Condition.INFERIEUR)
    armeeMoinsQue5 = condition.Condition(clovis.Clovis.C_MILITAIRE, 2, condition.Condition.INFERIEUR)

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
        # gestion du pillage
        gestionPillage = declencheur.Declencheur(proba.Proba(0.02, True), "gestionPillage")
        gestionPillage.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(gestionPillage)
        # antrustions
        probaAntrustion = proba.Proba(0.03, True)
        modifProbaAntrustion = modifProba.ModifProba(0.08, usurpationPlusQue4)
        probaAntrustion.ajouterModifProba(modifProbaAntrustion)
        antrustions = declencheur.Declencheur(probaAntrustion, "antrustions")
        antrustions.AjouterCondition(estRoi)
        antrustions.AjouterCondition(usurpationPlusQue2)
        selecteur_.ajouterDeclencheur(antrustions)
        # recrutement
        probarecrutement = proba.Proba(0.02, True)
        modifProbarecrutement = modifProba.ModifProba(0.06, armeeMoinsQue2)
        probarecrutement.ajouterModifProba(modifProbarecrutement)
        recrutement = declencheur.Declencheur(probarecrutement, "recrutement")
        recrutement.AjouterCondition(richessePlusQue0)
        recrutement.AjouterCondition(armeeMoinsQue5)
        recrutement.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(recrutement)
        # imp??ts
        impots = declencheur.Declencheur(proba.Proba(0.05, True), "impots")
        impots.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(impots)
        # corruption
        corruption = declencheur.Declencheur(proba.Proba(0.05, True), "corruption")
        corruption.AjouterCondition(estRoi)
        selecteur_.ajouterDeclencheur(corruption)
        # revolte_impots
        revolte_impots = declencheur.Declencheur(proba.Proba(0.04, True), "revolte_impots")
        revolte_impots.AjouterCondition(estRoi)
        revolte_impots.AjouterCondition(fideliteGauleMoinsQue0)
        selecteur_.ajouterDeclencheur(revolte_impots)
        # rentree_dimpots
        rentree_dimpots = declencheur.Declencheur(proba.Proba(0.04, True), "rentree_dimpots")
        rentree_dimpots.AjouterCondition(estRoi)
        rentree_dimpots.AjouterCondition(fideliteGaulePlusQue0)
        selecteur_.ajouterDeclencheur(rentree_dimpots)

label rentree_dimpots:
    "Les imp??ts rentrent bien."
    menu:
        "Qu'allez-vous faire de cette rentr??e d'argent."
        "Investir dans l'arm??e":
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
        "Garder cela dans vos coffres":
            $ AjouterACarac(trait.Richesse.NOM, 1)
        "Corrompre des nobles francs turbulents":
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
        "Organiser des jeux de cirque":
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
    jump fin_cycle

label revolte_impots:
    "En conqu??rant l'empire romain vous avez bien s??r repris leur int??ressant syst??me d'imp??ts directs et indirects qui alimente vos caisses r??guli??rement."
    "Mais cette ann??e les gaulois se rebellent et refusent de payer."
    $ testCombat = testDeCarac.TestDeCarac(clovis.Clovis.C_MILITAIRE, 3, situation_)
    $ testPolitique = testDeCarac.TestDeCarac(metier.Politique.NOM, 6, situation_)
    menu:
        "Comment g??rez-vous cette r??volte ?"
        "Leur accorder une dispense exceptionnelle.":
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
        "Envoyer l'arm??e les r??primer [testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Apr??s quelques ex??cutions et granges br??l??es les gaulois sont vite calm??s."
            else:
                "Les rebelles sont ??tonnament coriaces. Non seulement ils ne payent pas mais ils humilient vos soldats durant quelques escarmouches sanglantes."
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
        "N??gocier avec les notables pour calmer les tensions [testPolitique.affichage_]":
            $ reussi = testPolitique.TesterDifficulte(situation_)
            if reussi:
                "Apr??s quelques dures n??gociations la r??volte se calme pacifiquement."
            else:
                "Les rebelles pendent un de vos n??gociateurs et trainent votre nom dans la boue."
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
    jump fin_cycle

label corruption:
    scene bg cours_merovingienne
    with dissolve
    $ testImpots = testDeCarac.TestDeCarac([metier.Politique.NOM, clovis.Clovis.C_FIDELITE_GAULE], 5, situation_)
    menu:
        " "
        "Administrer les Gaules [testImpots.affichage_]":
            $ reussi = testImpots.TesterDifficulte(situation_)
            if reussi:
                "Votre administration est fiable et la corruption tr??s faible."
            else:
                "Vos fonctionnaires vous volent vous en ??tes s??r. Il va falloir s??vir."
                $ RetirerACarac(trait.Richesse.NOM, 1)
    jump fin_cycle

label recrutement:
    scene bg cours_merovingienne
    with dissolve
    menu:
        "Vous ??tes assez riche pour renforcer vos arm??es avec des mercenaires si vous le souhaitez."
        "Oui":
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
        "Non":
            pass

    jump fin_cycle

label impots:
    scene bg cours_merovingienne
    with dissolve
    $ testImpots = testDeCarac.TestDeCarac([metier.Politique.NOM, clovis.Clovis.C_FIDELITE_GAULE], 5, situation_)
    menu:
        "Allez vous r??ussir ?? pousser les gaulois ?? vous payer des imp??ts ?"
        "[testImpots.affichage_]":
            $ reussi = testImpots.TesterDifficulte(situation_)
            if reussi:
                "Gr??ce ?? vos efforts en leur faveur les galloromains vous sont favorables et suivent vos lois. Les imp??ts rentrent."
                $ AjouterACarac(trait.Richesse.NOM, 1)
            else:
                "Les gaulois sont sournois et d??sob??issants. Malgr?? vos efforts les rendements des imp??ts sont m??diocres."
                menu:
                    "Voulez vous autoriser vos soldats ?? piller quelques villes pour leur apprendre ?? ob??ir ?"
                    "Oui":
                        "Les pillages vous rapportent et d??foulent vos soldats mais les gaulois vous d??testent encore plus."
                        $ AjouterACarac(trait.Richesse.NOM, 1)
                        $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
                        $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
                    "Non":
                        pass
    jump fin_cycle

label antrustions:
    scene bg cours_merovingienne
    with dissolve
    "Les francs sont m??contents, vous vous sentez menac??."
    "Peut-??tre est-ce le moment de nommer de nouveaux antrustions. Ces huerriers d'??lite de confiance ont des privil??ges divers et sont bien pay??s."
    "Ils sont surtout si fid??les qu'ils feront barrage de leur corps pour vous prot??ger."
    menu:
        "Engager des antrustions ?"
        "Oui":
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
        "Non":
            jump fin_cycle
    jump fin_cycle

label gestionPillage:
    scene bg cours_merovingienne
    with dissolve
    $ nomSenateur = gaulois_.CreerPrenom(True)
    "Le s??nateur gallo-romain [nomSenateur] vient ?? vous se plaindre humblement des pillages caus??s par vos guerriers et vous demande d'y mettre un terme."
    menu:
        "Interdire le pillage sous peine de mort":
            "Les guerriers prennent tr??s mal cet affront ?? la coutume. Ils doivent acheter et entretenir leur propre mat??riel. ?? quoi bon si ils ne peuvent pas se payer sur les vaincus ?"
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 3)
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
            jump fin_cycle
        "R??primander les soldats":
            "Les guerriers prennent mal la r??primande. Ils doivent acheter et entretenir leur propre mat??riel. ?? quoi bon si ils ne peuvent pas se payer sur les vaincus ?"
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            jump fin_cycle
        "Le renvoyer s??chement. Vae Victis !":
            $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            jump fin_cycle
        "L'ex??cuter pour son insolence":
            $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
            jump fin_cycle

    jump fin_cycle

label comtCritique:
    scene bg cours_merovingienne
    with dissolve
    $ nomComte = gaulois_.CreerPrenom(True)
    "Le comte [nomComte] ?? votre service se comporte para??t-til comme un brigand. Il vole et frappe ses sujets et les plaintes s'accumulent."
    "Il est par contre d'une fid??lit?? ?? toute ??preuve envers vous et fait rentrer les imp??ts tr??s efficacement."
    menu:
        "Le r??primander publiquement":
            "Les galloromains appr??cident de voir que leurs demandes sont entendues. Le comte [nomComte] n'ose plus les pressurer autant qu'avant."
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
            jump fin_cycle

        "Le faire ex??cuter":
            "Le peuple est satisfait de voir son tourmenteur mort, mais les autres comtes sont terrifi??s de voir que la fid??lit?? envers vous ne leur garantit pas votre cl??mence."
            $ RetirerACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
            jump fin_cycle

        "le laisser agir ?? sa guise tant que les imp??ts entrent":
            "Le peuple est ??cras?? mais l'argent coule ?? flot."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 2)
            jump fin_cycle

        "le remplacer discr??tement":
            "Les galloromains appr??cident de voir que leurs demandes sont entendues."
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 1)
            jump nommageComte
    jump fin_cycle


label nommageComte:
    scene bg cours_merovingienne
    with dissolve
    $ nomComte1 = francs_.CreerPrenom(True)
    $ nomComte2 = gaulois_.CreerPrenom(True)
    $ nomComte3 = gaulois_.CreerPrenom(True)
    $ nomComte4 = francs_.CreerPrenom(True)
    "Le comte est un fonctionnaire de haut rang responsable entre autres de la collecte des imp??ts."
    menu:
        "[nomComte1], un franc juste et intransigeant":
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
            jump fin_cycle
        "[nomComte2], un gaulois aim?? du peuple":
            $ AjouterACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            jump fin_cycle
        "[nomComte3], un affranchi malin et d??vou?? qui saura faire rentrer les imp??ts":
            "[nomComte3] est en effet dou?? et efficace mais il se fait vite d??tester par tout le royaume."
            $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ AjouterACarac(trait.Richesse.NOM, 1)
            jump fin_cycle
        "[nomComte4], un ancien officier, sp??cialiste du recrutement":
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
    jump fin_cycle

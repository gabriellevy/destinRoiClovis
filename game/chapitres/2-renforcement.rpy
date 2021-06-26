
init -5 python:
    import random
    from despin.gen_vie import declencheur
    from despin.gen_vie import selecteur
    from despin.gen_vie import proba
    from despin.abs import condition
    from humanite import trait
    from humanite import pnj
    from humanite import metier
    from univers import temps
    # from geographie import quartier
    from humanite import identite
    from chapitres.classes import syagrius


    auMoinsAnnee485 = condition.Condition(temps.Date.DATE_ANNEES, 485, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee482 = condition.Condition(temps.Date.DATE_ANNEES, 482, condition.Condition.SUPERIEUR_EGAL)
    # conditions syagrius
    syagriusPasVaincu = condition.Condition(syagrius.Syagrius.C_VAINCU, 1, condition.Condition.DIFFERENT)
    syagriusVaincu = condition.Condition(syagrius.Syagrius.C_VAINCU, 1, condition.Condition.EGAL)
    stabiliteSyagriusFaible = condition.Condition(syagrius.Syagrius.C_STABILITE, 0, condition.Condition.INFERIEUR)
    armeeSyagriusFaible = condition.Condition(syagrius.Syagrius.C_STABILITE, 3, condition.Condition.INFERIEUR)
    def MiseEnPlaceCaracsSyagrius():
        global situation_
        situation_.SetValCarac(syagrius.Syagrius.C_VAINCU, 0)
        situation_.SetValCarac(syagrius.Syagrius.C_GUERRE, 0)
        situation_.SetValCarac(syagrius.Syagrius.C_STABILITE, 2)
        situation_.SetValCarac(syagrius.Syagrius.C_MILITAIRE, 6)

    def AjouterEvtRenforcement481_485():
        global selecteur_
        miner_le_royaume = declencheur.Declencheur(proba.Proba(0.2, True), "miner_le_royaume")
        miner_le_royaume.AjouterCondition(estRoi)
        miner_le_royaume.AjouterCondition(syagriusPasEnGuerre)
        miner_le_royaume.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(miner_le_royaume)

        mort_euric = declencheur.Declencheur(proba.Proba(0.5, False), "mort_euric")
        mort_euric.AjouterCondition(auMoinsAnnee485)
        mort_euric.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(mort_euric)

        probaAttaqueRoyaume = proba.Proba(0.0, True)
        probaAttaqueRoyaume.ajouterModifProbaViaVals(0.25, stabiliteSyagriusFaible)
        probaAttaqueRoyaume.ajouterModifProbaViaVals(0.25, armeeSyagriusFaible)
        choixAttaqueDuRoyaume = declencheur.Declencheur(probaAttaqueRoyaume, "choixAttaqueDuRoyaume")
        choixAttaqueDuRoyaume.AjouterCondition(syagriusPasEnGuerre)
        choixAttaqueDuRoyaume.AjouterCondition(auMoinsAnnee482)
        choixAttaqueDuRoyaume.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(choixAttaqueDuRoyaume)

label choixAttaqueDuRoyaume:
    menu:
        "Le royaume de Syagrius est très affaibli."
        "L'attaquer.":
            jump attaqueSyagrius
        "Attendre encore un peu que votre position soit meilleure.":
            jump fin_cycle

label mort_euric:
    # Mort d'Eulric roi des wisigoths
    "Excellente nouvelle : Euric le grand des Wisigoths et meilleur allié de Syagrius est mort. Syagrius va être très affaibli et sans soutien étranger face à vous."
    $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 2)
    $ RetirerACarac(syagrius.Syagrius.C_MILITAIRE, 2)

label miner_le_royaume:
    # si Clovis mais ne possède pas encore le royaume de Syagrius
    $ nb_miner_le_royaume = situation_.GetValCaracInt("nb_miner_le_royaume")
    $ a_corrompu_senateurs = situation_.GetValCaracBool("a_corrompu_senateurs")
    $ a_contacte_eveque = situation_.GetValCaracBool("a_contacte_eveque")
    $ a_convaincu_chararic = situation_.GetValCaracBool("a_convaincu_chararic")
    $ a_convaincu_ragnacaire = situation_.GetValCaracBool("a_convaincu_ragnacaire")
    if nb_miner_le_royaume == 0:
        $ situation_.SetValCarac("nb_miner_le_royaume", 1)
        "Vos francs sont les meilleurs guerriers du monde, vous en êtes sûr. Avant même la mort de votre père vous saviez déjà que grâce à eux vous pourriez franchir la première marche qui mène à la gloire et la richesse :"
        "Conquérir le royaume romain de Syagrius."
        "Ce royaume est en apparence grand et riche mais vous savez qu'il est désuni et fragile."
        # A FAIRE : afficher carte de l'époque
        "Pour l'instant vous n'êtes pas prêt d'autant plus que Syagrius le romain est allié à Euric le puissant roi des Wisigoths. Mais votre destin est déjà tracé."

    menu:
        "Comment allez vous affaiblir Syagrius ?"
        "Convaincre votre parent, le prince franc Chararic, de vous rejoindre" if not a_convaincu_chararic:
            "Chararic accept l'alliance mais laisse bien clair qu'il s'agit d'une alliance et pas d'une soumission : vous êtes son égal et ne serez jamaias son supérieur."
            $ situation_.SetValCarac("a_convaincu_chararic", 1)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
        "Chercher l'appui de Ragnacaire, le roi franc de Cambrai" if not a_convaincu_ragnacaire:
            "Chararic accept l'alliance mais laisse bien clair qu'il s'agit d'une alliance et pas d'une soumission : vous êtes son égal et ne serez jamaias son supérieur."
            $ situation_.SetValCarac("a_convaincu_ragnacaire", 1)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
        "Tenter de pactiser avec les sénateurs romains du territoire de Syagrius" if not a_corrompu_senateurs:
            "Les romains semblent avoir peur que vous détruisiez ce qui reste du système romain. Ils préfèrent encore Syagrius à vous et vous n'en tirez rien de bon."
            $ situation_.SetValCarac("a_corrompu_senateurs", 1)
            jump fin_cycle
        "Corrompre ses soldats":
            "Les romains sont comme les autres. Pour un peu d'or et des promesses de pillage ils vous rejoignent."
            $ RetirerACarac(syagrius.Syagrius.C_MILITAIRE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 2)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
        "Tenter de gagner les faveurs des évèques" if not a_contacte_eveque:
            "À votre grande surprise les évèques vous préfèrent, vous le roi païen, aux autres barbares qui sont des chrétiens ariens hérétiques."
            "Sans doute pensent-ils pouvoir plus facilement vous convertir, vous et vos hommes. Il est vrai que vous êtes souvent touchés par leurs arguments religieux."
            "Quoiqu'il en soit, si vous envahissez le royaume ils pousseront le peuple à vous soutenir et à abandonner Syagrius."
            $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 2)
            $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 1)
            $ situation_.SetValCarac("a_contacte_eveque", 1)
            jump fin_cycle
        "Vous contenter d'attendre le moment opportun.":
            jump fin_cycle
    jump fin_cycle

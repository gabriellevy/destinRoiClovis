
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
    # from geographie import quartier
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import clovis

    auMoinsAnnee485 = condition.Condition(temps.Date.DATE_ANNEES, 485, condition.Condition.SUPERIEUR_EGAL)
    auMoinsAnnee482 = condition.Condition(temps.Date.DATE_ANNEES, 482, condition.Condition.SUPERIEUR_EGAL)
    # conditions syagrius
    syagriusPasVaincu = condition.Condition(syagrius.Syagrius.C_ETAT, syagrius.Syagrius.INDEMNE, condition.Condition.EGAL)
    syagriusVaincu = condition.Condition(syagrius.Syagrius.C_ETAT, syagrius.Syagrius.INDEMNE, condition.Condition.DIFFERENT)

    stabiliteSyagriusFaible = condition.Condition(syagrius.Syagrius.C_STABILITE, 0, condition.Condition.INFERIEUR)
    armeeSyagriusFaible = condition.Condition(syagrius.Syagrius.C_MILITAIRE, 3, condition.Condition.INFERIEUR)
    stabiliteSyagriusPasFaible = condition.Condition(syagrius.Syagrius.C_STABILITE, 0, condition.Condition.SUPERIEUR)
    armeeSyagriusPasFaible = condition.Condition(syagrius.Syagrius.C_MILITAIRE, 3, condition.Condition.SUPERIEUR)

    euricVivant = condition.Condition("euricMort", 1, condition.Condition.DIFFERENT)
    def MiseEnPlaceCaracsSyagrius():
        global situation_
        situation_.SetValCarac(syagrius.Syagrius.C_ETAT, syagrius.Syagrius.INDEMNE)
        situation_.SetValCarac(syagrius.Syagrius.C_STABILITE, 2)
        situation_.SetValCarac(syagrius.Syagrius.C_MILITAIRE, 6)
        situation_.SetValCarac(syagrius.Syagrius.C_PILLAGE, 0)

    def AjouterEvtRenforcement481_485():
        global selecteur_
        probaminer_le_royaume = proba.Proba(0.2, True)
        probaminer_le_royaume.ajouterModifProbaViaVals(-0.1, stabiliteSyagriusFaible)
        probaminer_le_royaume.ajouterModifProbaViaVals(-0.1, armeeSyagriusFaible)
        miner_le_royaume = declencheur.Declencheur(probaminer_le_royaume, "miner_le_royaume")
        miner_le_royaume.AjouterCondition(estRoi)
        miner_le_royaume.AjouterCondition(syagriusPasEnGuerre)
        miner_le_royaume.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(miner_le_royaume)

        mort_euric = declencheur.Declencheur(proba.Proba(0.5, False), "mort_euric")
        mort_euric.AjouterCondition(auMoinsAnnee485)
        mort_euric.AjouterCondition(syagriusPasVaincu)
        mort_euric.AjouterCondition(euricVivant)
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
    $ AfficherCarteActuelle()
    with dissolve
    menu:
        "Le royaume de Syagrius est tr??s affaibli."
        "L'attaquer.":
            jump invasion_syagrius
        "Attendre encore un peu que votre position soit meilleure.":
            jump fin_cycle

label mort_euric:
    # Mort d'Eulric roi des wisigoths
    $ AfficherCarteActuelle()
    with dissolve
    "Excellente nouvelle : Euric le grand des Wisigoths et meilleur alli?? de Syagrius est mort. Syagrius va ??tre tr??s affaibli et sans soutien ??tranger face ?? vous."
    $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 2)
    $ RetirerACarac(syagrius.Syagrius.C_MILITAIRE, 2)
    $ situation_.SetValCarac("euricMort", 1)
    jump choixAttaqueDuRoyaume

label miner_le_royaume:
    $ AfficherCarteActuelle()
    with dissolve
    # si Clovis mais ne poss??de pas encore le royaume de Syagrius
    $ nb_miner_le_royaume = situation_.GetValCaracInt("nb_miner_le_royaume")
    $ a_corrompu_senateurs = situation_.GetValCaracBool("a_corrompu_senateurs")
    $ a_contacte_eveque = situation_.GetValCaracBool("a_contacte_eveque")
    $ a_convaincu_chararic = situation_.GetValCaracBool("a_convaincu_chararic")
    $ a_convaincu_ragnacaire = situation_.GetValCaracBool("a_convaincu_ragnacaire")
    # tmp
    $ C_STABILITE = situation_.GetValCaracInt(syagrius.Syagrius.C_STABILITE)
    $ print("C_STABILITE : {}".format(C_STABILITE))
    $ C_MILITAIRE = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    $ print("C_MILITAIRE : {}".format(C_MILITAIRE))
    $ etatSyag = situation_.GetValCarac(syagrius.Syagrius.C_ETAT)
    $ print("etat Syagrius : {}".format(etatSyag))
    # fin tmp
    if nb_miner_le_royaume == 0:
        $ situation_.SetValCarac("nb_miner_le_royaume", 1)
        "Vos francs sont les meilleurs guerriers du monde, vous en ??tes s??r. Avant m??me la mort de votre p??re vous saviez d??j?? que gr??ce ?? eux vous pourriez franchir la premi??re marche qui m??ne ?? la gloire et la richesse :"
        $ AfficherCarteActuelle()
        "Conqu??rir le royaume romain de Syagrius."
        "Ce royaume est en apparence grand et riche mais vous savez qu'il est d??suni et fragile."
        "Pour l'instant vous n'??tes pas pr??t d'autant plus que Syagrius le romain est alli?? ?? Euric le puissant roi des Wisigoths. Mais votre destin est d??j?? trac??."

    menu:
        "Comment allez vous affaiblir Syagrius ?"
        "Convaincre votre parent, le prince franc Chararic, de vous rejoindre" if not a_convaincu_chararic:
            "Chararic accepte l'alliance mais laisse bien clair qu'il s'agit d'une alliance et pas d'une soumission : vous ??tes son ??gal et ne serez jamais son sup??rieur."
            $ situation_.SetValCarac("a_convaincu_chararic", 1)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
        "Chercher l'appui de Ragnacaire, le roi franc de Cambrai" if not a_convaincu_ragnacaire:
            "Ragnacaire accepte l'alliance mais laisse bien clair qu'il s'agit d'une alliance et pas d'une soumission : vous ??tes son ??gal et ne serez jamais son sup??rieur."
            $ situation_.SetValCarac("a_convaincu_ragnacaire", 1)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
        "Tenter de pactiser avec les s??nateurs romains du territoire de Syagrius" if not a_corrompu_senateurs:
            "Les romains semblent avoir peur que vous d??truisiez ce qui reste du syst??me romain. Ils pr??f??rent encore Syagrius ?? vous et vous n'en tirez rien de bon."
            $ situation_.SetValCarac("a_corrompu_senateurs", 1)
            jump fin_cycle
        "Corrompre ses soldats":
            "Les romains sont comme les autres. Pour un peu d'or et des promesses de pillage ils vous rejoignent."
            $ RetirerACarac(syagrius.Syagrius.C_MILITAIRE, 1)
            $ RetirerACarac(trait.Richesse.NOM, 2)
            $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
            jump fin_cycle
        "Tenter de gagner les faveurs des ??v??ques" if not a_contacte_eveque:
            "?? votre grande surprise les ??v??ques vous pr??f??rent, vous le roi pa??en, aux autres barbares qui sont des chr??tiens ariens h??r??tiques."
            "Sans doute pensent-ils pouvoir plus facilement vous convertir, vous et vos hommes. Il est vrai que vous les ??coutez poliment et ??tes souvent touch?? par leurs arguments religieux."
            "Quoiqu'il en soit, si vous envahissez le royaume ils pousseront le peuple ?? vous soutenir et ?? abandonner Syagrius."
            $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 2)
            $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 1)
            $ situation_.SetValCarac("a_contacte_eveque", 1)
            jump fin_cycle
        "Vous contenter d'attendre le moment opportun.":
            jump fin_cycle
    jump fin_cycle

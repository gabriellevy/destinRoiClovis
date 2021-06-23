
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


    syagriusPasVaincu = condition.Condition(syagrius.Syagrius.C_VAINCU, 1, condition.Condition.DIFFERENT)
    syagriusVaincu = condition.Condition(syagrius.Syagrius.C_VAINCU, 1, condition.Condition.EGAL)
    auMoinsAnnee485 = condition.Condition(temps.Date.DATE_ANNEES, 485, condition.Condition.SUPERIEUR_EGAL)
    def MiseEnPlaceCaracsSyagrius():
        global situation_
        situation_.SetValCarac(syagrius.Syagrius.C_VAINCU, 0)
        situation_.SetValCarac(syagrius.Syagrius.C_GUERRE, 0)
        situation_.SetValCarac(syagrius.Syagrius.C_STABILITE, 2)
        situation_.SetValCarac(syagrius.Syagrius.C_MILITAIRE, 7)

    def AjouterEvtRenforcement481_485():
        global selecteur_
        miner_le_royaume = declencheur.Declencheur(proba.Proba(0.2, True), "miner_le_royaume")
        miner_le_royaume.AjouterCondition(estRoi)
        miner_le_royaume.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(miner_le_royaume)

        mort_euric = declencheur.Declencheur(proba.Proba(0.5, False), "mort_euric")
        mort_euric.AjouterCondition(auMoinsAnnee485)
        mort_euric.AjouterCondition(syagriusPasVaincu)
        selecteur_.ajouterDeclencheur(mort_euric)


label mort_euric:
    # Mort d'Eulric roi des wisigoths
    menu:
        "mort_euric"
        "ok":
            pass

    "Excellente nouvelle : Euric le grand des Wisigoths et meilleur allié de Syagrius est mort. Sa position va être très affaiblie."
    $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 2)
    $ RetirerACarac(syagrius.Syagrius.C_MILITAIRE, 2)

label miner_le_royaume:
    # si Clovis mais ne possède pas encore le royaume de Syagrius
    menu:
        "Miner le royaume !"
        "ok":
            pass

    $ nb_miner_le_royaume = situation_.GetValCaracInt("nb_miner_le_royaume")
    if nb_miner_le_royaume == 0:
        $ situation_.SetValCarac("nb_miner_le_royaume", 1)
        "Vos francs sont les meilleurs guerriers du monde, vous en êtes sûr. Avant même la mort de votre père vous saviez déjà que grâce à eux vous pouviez franchir la prmeière marche qui mène à la gloir et la richesse :"
        "Conquérir le royaume romain de Syagrius."
        "Ce royaume est en apparence grand et riche ais vous savez qu'il est désuni et fragile."
        # A FAIRE : afficher carte de l'époque
        "Pour l'instant vous n'êtes pas prêt d'autant plus que Syagrius le romain est allié à Euric le puissant roi des Wisigoths. Mais votre destin est déjà tracé."
    else:
        "Vous vous employez à affaiblir le royaume de Siagrius."
    jump fin_cycle

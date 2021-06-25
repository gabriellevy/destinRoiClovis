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
    from humanite import identite
    from chapitres.classes import syagrius

    # conditions syagrius
    syagriusEnGuerre = condition.Condition(syagrius.Syagrius.C_GUERRE, 1, condition.Condition.EGAL)
    syagriusPasEnGuerre = condition.Condition(syagrius.Syagrius.C_GUERRE, 1, condition.Condition.DIFFERENT)
    def MiseEnPlaceGuerreSyagrius():
        global situation_
        situation_.SetValCarac(syagrius.Syagrius.C_GUERRE, 1)

    def AjouterEvtGuerreSyagrius():
        global selecteur_
        combat_avant_garde = declencheur.Declencheur(proba.Proba(0.2, True), "combat_avant_garde")
        combat_avant_garde.AjouterCondition(syagriusEnGuerre)
        selecteur_.ajouterDeclencheur(combat_avant_garde)

label combat_avant_garde:
    "Votre avant-garde se heurte à une petite armée romaine."
    $ puissanceArmeeSyagrius = situation_.GetValCaracInt(syagrius.Syagrius.C_MILITAIRE)
    $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE], puissanceArmeeSyagrius, situation_)
    menu:
        "vos ordres sont d'éviter le combat":
            "Vos cavaliers parviennent facilement à échapper aux romains lourds et malabiles."
            jump fin_cycle
        "Au combat ! [testCombat.affichage_]":
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Vos hommes écrasent facilement ces mauvais militaires et pillent la région."
                $ RetirerACarac(syagrius.Syagrius.C_STABILITE, 1)
            else:
                "Vos cavaliers sont incapables de briser la cohorte romaine et s'enfuient. C'est une défaite cuisante. Sans importance stratégique mais humiliante."
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
            jump fin_cycle


label attaqueSyagrius:
    $ MiseEnPlaceGuerreSyagrius()
    # lancer un défi ????
    jump fin_cycle

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

label invasion_syagrius:
    $ MiseEnPlaceGuerreSyagrius()
    "Votre armée est maintenant bien avancée en territoire ennemi et vous savez que Syagrius a fini de lever la sienne."
    menu:
        "Si vous suivez la coutume franque de le défier sur le champs de bataille de son choix.":
            "Syagrius accepte le défi et choisit un champs près de sa capitale Soissons."
            "Vos hommes sont pressés d'en venir aux mains et sont heureux que vous ayez respecté les lois d'Odin. Thor et les walkyrie vous soutiendront."
            $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
        "Si vous vous dirigez vers sa capitale Soissons pour l'écraser le plus tôt possible.":
            "Syagrius semble vouloir éviter un siège et vient à votre rencontre. Heureusement pour vous car la prise de ville n'est pas la spécialité de vos guerrier."
        "Si vous avancez lentement et prenez le temps de piller le pays.":
            "Les terres romaines sont bien plus riches que les vôtres. Vous faites un grand buton de richesse et d'esclaves. Vos hommes sont satisfaits."
            "Syagrius quitte Soissons pour vnir vous arrêter. Heureusement pour vous car la prise de ville n'est pas la spécialité de vos guerrier."
            $ AjouterACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(syagrius.Syagrius.C_PILLAGE, 2)
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)

    jump bataille_soisson

label bataille_soisson:
    "A FAIRE : bataille de Soissons."
    jump fin_cycle

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
                $ AjouterACarac(syagrius.Syagrius.C_PILLAGE, 1)
            else:
                "Vos cavaliers sont incapables de briser la cohorte romaine et s'enfuient. C'est une défaite cuisante. Sans importance stratégique mais humiliante."
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
            jump fin_cycle

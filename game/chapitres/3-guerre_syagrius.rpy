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
    scene bg francs
    "{b}Bataille de Soissons.{/b}"
    "Syagrius a rangé son armée de manière ordonnée à la romaine. Mais la discipline apparente ne vous impressionne pas. La plupart des sodats sont des germains qui combatront sans grand entousiasme."
    menu:
        "D'où allez vous combattre ?"
        "Au premier rang !":
            jump bataille_soisson_combat
        "En soutien au second rang.":
            "Vous faites avancer votre armée en bon ordre. Les soldats sont motivés par votre présence et veulent se faire remarquer par leur bravoure."
            $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
            menu:
                "Les romains se préparent au choc. [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Vos hommes dominent si bien la bataille que votre première ligne semble suffire à repousser les romains."
                        jump bataille_soisson_2
                    else:
                        "La première ligne est enfoncée. Vous allez devoir aller au contact avec votre garde d'honneur pour la soutenir."
                        jump bataille_soisson_combat

        "En retrait pour avoir une vue d'ensemble et rester en sécurité.":
            "De puis une petite colline vous donnez vos ordres pour faire avancer votre infanterie."
            "Vos soldats obéissent restent confiants et disciplinés mais il est clair qu'ils apprécient peu que le descendant des dieux que vous êtes reste à l'arrière."
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
            $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeSyagrius, situation_)
            menu:
                "Les romains se préparent au choc. [testCombat.affichage_]":
                    $ reussi = testCombat.TesterDifficulte(situation_)
                    if reussi:
                        "Vos hommes dominent si bien la bataille que votre première ligne semble suffire à repousser les romains."
                        jump bataille_soisson_2
                    else:
                        "Les pertes sont lourdes mais vos soldats sont meilleurs et plus motivés. Ils prennent l'avantage."
                        $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
                        jump bataille_soisson_2

    label bataille_soisson_combat:
        "Vous formez un groupe compact avec l'élite de vos hommes et avancez droit sur le centre ennemi."
        "Les romains tentent de rester en formation serrée avec leur boucliers levés. Vous ordonnez alors à vos hommes de lancer leurs lourds javelots à crochet."
        "La plupart sont bloqués par les boucliers ennemis mais ils sont si lourds et solides que les romains ne peuvent plus manoeuvrer et peinent à lever leurs boucliers."
        $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 4, situation_)
        menu:
            "C'est le moment de lancer une charge complète.[testCombat.affichage_]":
                $ reussi = testCombat.TesterDifficulte(situation_)
                if not reussi:
                    "Alors que vous atteignez les lignes ennemies un javelot bien lancé vous frappe en plein visage. Votre court règne s'arrête ici."
                    jump mort
                else:
                    "Vous avez repéré un officier empêtré par un javelot dans son bouclier. Vous écartez le bouclier d'un coup de pied dans le javelot et poignardez facilement son corps découvert avec votre scramasax."
                    $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                    $ testCombat = testDeCarac.TestDeCarac(metier.Guerrier.NOM, 7, situation_)
                    menu:
                        "Enhardi vous vous jetez en avant en chantant à la gloire d'Odin.[testCombat.affichage_]":
                            $ reussi = testCombat.TesterDifficulte(situation_)
                            if reussi:
                                "Vous empoignez votre francisque et faites un grand massacre des romains terrifiés et désordonnés."
                                $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                                jump bataille_soisson_2
                            else:
                                "Vous avez été repéré et une volée de javelot s'abat sur vous. Votre bouclier tient le choc mais les pointent le traversent et s'arrêtent à un doigt de votre visage."
                                "Sous le choc, vous êtes heureusement secourus par vos fidèles gardes du corps qui couvrent votre corps de leurs boucliers."
                                jump bataille_soisson_2

    jump bataille_soisson_2

label bataille_soisson_2:
    scene bg francs
    menu:
        "BAtaille de soissons 2 ème choc"
        "ok":
            pass
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

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
    from abs.humanite import identite
    from chapitres.classes import syagrius
    from chapitres.classes import clovis

    def AjouterEvtThuringie():
        global selecteur_
        guerre_thuringie491 = dec_clo.DecClovisU(proba.Proba(0.4, True), "guerre_thuringie491", 490)
        selecteur_.ajouterDeclencheur(guerre_thuringie491)

        ragnacaire = dec_clo.DecClovisU(proba.Proba(0.3, True), "ragnacaire", 487)
        selecteur_.ajouterDeclencheur(ragnacaire)

label ragnacaire:
    play music guerre1 noloop
    $ puissanceArmeeRagnacaire = 4
    "Ragnacaire est un roi faible car ses débauches, qui vont jusqu'à l'inceste, le font détester même par ses propres hommes."
    $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeRagnacaire, situation_)
    $ testRuse = testDeCarac.TestDeCarac([trait.Ruse.NOM, metier.Politique.NOM], 3, situation_)
    menu:
        "Comment l'éliminer : "
        "Préparer l'invasion [testCombat.affichage_]":
            $ situation_.AvanceDeXMois(1)
            $ reussi = testCombat.TesterDifficulte(situation_)
            if reussi:
                "Vous écrasez la faible armée de Ragnacaire et l'exécutez promptement de vos propres mains, ainsi que son frère. Devant votre valeur, ses hommes survivants se rallient à vous sans discuter."
                $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
                $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
                jump fin_cycle
            else:
                "Quoiqu'inférieures en nombre les troupes de Ragnacaire vous infligent une grave défaite. Cet échec humiliant affaiblit grandement votre crédibilité."
                $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
                $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
                $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
                jump fin_cycle
            jump fin_cycle
        "Provoquer la trahison de ses hommes par ruse [testRuse.affichage_]":
            $ reussi = testRuse.TesterDifficulte(situation_)
            $ situation_.AvanceDeXMois(1)
            if reussi:
                "Ragnacaire est méprisé par ses propres guerriers, vous parvenez à en soudoyer suffisament pour qu'ils vous le livrent. Après quoi vous l'excutez d'un coup de hache ainsi que son frère."
                "Ses autres hommes se rallient à vous facilement."
                $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
                jump fin_cycle
            else:
                "Ragnacaire se doute de quelque chose et parvient à déjouer les pièges et éliminer vos espions. Vous vous êtes fait un ennemi mortel."
                $ AjouterACarac(clovis.Clovis.C_USURPATION, 2)
                jump fin_cycle
            jump fin_cycle

        "Le laisser en paix":
            "Vous laissez Ragnacaire à ses débauches et il vous laisse à vos ambitions. Sa cour devient néanmoins un vrai nid de conspirateurs."
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            jump fin_cycle

    jump fin_cycle

label guerre_thuringie491:
    play music guerre1 noloop
    $ situation_.SetValCarac(clovis.Clovis.C_STATUT_CHARARIC, clovis.Clovis.CHARARIC_ROI)
    $ puissanceArmeeChararic = 4
    "La Thuringie est une nuisance certes faible mais dangereuse car sur vos arrières."
    "Chararic leur roi a déjà montré son manque de fiabilité en intervenant à la bataille de Soissons seulement une fois que votre victoire était assurée."
    $ testCombat = testDeCarac.TestDeCarac([clovis.Clovis.C_MILITAIRE, metier.Stratege.NOM], puissanceArmeeChararic, situation_)
    $ testRuse = testDeCarac.TestDeCarac(trait.Ruse.NOM, 2, situation_)
    label guerre_thuringie491_decision:
        menu:
            "Il faut régler cela."
            "Préparer l'invasion de la Thuringie. [testCombat.affichage_]":
                jump guerre_thuringie491_bataille
            "Ruser pour capturer Chararic. [testRuse.affichage_]":
                jump guerre_thuringie491_ruse
            "Ordonner qu'il se soumette à vous formellement.":
                jump guerre_thuringie491_vassalisation

    label guerre_thuringie491_bataille:
        $ reussi = testCombat.TesterDifficulte(situation_)
        if reussi:
            "Vous écrasez la faible armée de Chararic et parvenez à le capturer."
            $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
            jump guerre_thuringie491_sort_chararic
        else:
            "Quoiqu'inférieures en nombre les troupes de Chararic vous infligent une grave défaite. Cet échec humiliant affaiblit grandement votre crédibilité."
            $ RetirerACarac(clovis.Clovis.C_MILITAIRE, 1)
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            $ RetirerACarac(clovis.Clovis.C_GLOIRE, 1)
            $ situation_.AvanceDeXMois(1)
            jump guerre_thuringie491_decision

    label guerre_thuringie491_ruse:
        $ reussi = testRuse.TesterDifficulte(situation_)
        if reussi:
            "Chararic est affaibli et peu aimé, vous parvenez à soudoyer suffisament de ses hommes pour qu'ils vous l'amènent pieds et poings liés.."
            jump guerre_thuringie491_sort_chararic
        else:
            "Chararic se doute de quelque chose et parvient à déjouer les pièges et éliminer vos espions."
            $ situation_.AvanceDeXMois(2)
            jump guerre_thuringie491_decision

    label guerre_thuringie491_sort_chararic:
        "Vous avez Chararic et son fils à votre merci. Ils savent que leur royaume est désormais entre vos mains mais ils ignorent quel sera leur sort."
        menu:
            "Qu'allez-vous leur faire ?"
            "Les libérer pour en faire des vassaux":
                jump guerre_thuringie491_vassalisation
            "Les tonsurer et les forcer à se faire moines":
                jump guerre_thuringie491_tonsurage
            "Les faire exécuter":
                jump guerre_thuringie491_execution


    label guerre_thuringie491_tonsurage:
        $ situation_.SetValCarac(clovis.Clovis.C_STATUT_CHARARIC, clovis.Clovis.CHARARIC_TONSURE)
        "En tonsurant des nobles vous prouvez leur faiblesse car leur chevelure est le sylbole de leur ascendance divine."
        "Une fois dans un monastère, tondus et en robe ils n'inspireront plus jamais le respect à des guerriers francs dignes de ce nom."
        $ fils = francs_.CreerPrenom(True)
        $ std = Character(fils)
        "Le jeune [fils], fils de Chararic, se permet néanmoins une bravade."
        std "Ne crains rien père, cela repoussera."
        "Il n'a pas tout à fait tort."
        menu:
            "Si vous préférez finalement les exécuter":
                "Vous fracassez subitement le crâne de [fils] à coup de hache, puis celui de son père."
                jump guerre_thuringie491_execution
            "Sinon":
                jump fin_cycle

    label guerre_thuringie491_vassalisation:
        "Chararic reconnaît votre supériorité et se soumet à vous en présence de ses hommes. Il est cependant évident qu'il est humilié et vous trahira si l'occasion se présente."
        $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
        $ AjouterACarac(clovis.Clovis.C_USURPATION, 2)
        $ situation_.SetValCarac(clovis.Clovis.C_STATUT_CHARARIC, clovis.Clovis.CHARARIC_VASSAL)
        jump fin_cycle

    label guerre_thuringie491_execution:
        "Bien que peu glorieuse, cette élimination des nobles est le meilleur moyen d'éviter qu'on remette en cause votre autorité."
        $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
        $ situation_.SetValCarac(clovis.Clovis.C_STATUT_CHARARIC, clovis.Clovis.CHARARIC_MORT)
        "Chararic mort, beaucoup de ses hommes vous rejoignent."
        $ AjouterACarac(clovis.Clovis.C_MILITAIRE, 1)
        $ valAltruisme = situation_.GetValCaracInt(trait.Altruisme.NOM)
        menu:
            "Peut-être qu'il serait plus prudent d'éliminer aussi tous les héritiers mâles de Chararic."
            "C'est dur mais plus prudent" if valAltruisme <= trait.Trait.SEUIL_A_PAS_EXTREME:
                "Vous éliminez ses enfants et tous ses neveux dont plusieurs jeunes enfants. Même les féroces francs trouvent que vous êtes allés loin et votre cruauté est connue dans toute la Gaulle."
                "Il n'empêche que moins il y aura de nobles, surtout dans les familles rivales, plus votre trône sera assuré."
                $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
                $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            "Non cela va trop loin.":
                jump fin_cycle
        jump fin_cycle

    jump fin_cycle

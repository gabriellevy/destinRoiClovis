init -5 python:
    import random
    from abs.religions import religion
    from abs import declencheur
    from abs import selecteur
    from abs import proba
    from abs import condition
    from abs.humanite import trait
    from abs.humanite import metier

    estPaien = condition.Condition(metier.Guerrier.NOM, trait.Trait.SEUIL_A_EXTREME, condition.Condition.INFERIEUR)

    def AjouterEvtsPaganisme():
        global selecteur_
        # divinité tutélaire
        diviniteTutelaire = declencheur.DeclencheurU(proba.Proba(0.05, True), "diviniteTutelaire")
        diviniteTutelaire.AjouterCondition(estPaien)
        selecteur_.ajouterDeclencheur(diviniteTutelaire)
        # punition par noyage d'adultère
        noyagePourAdultere = declencheur.DeclencheurU(proba.Proba(0.05, True), "noyagePourAdultere")
        selecteur_.ajouterDeclencheur(noyagePourAdultere)
        # victoire et prières des païens et des chrétiens
        prieresPaiennesChretiennes = declencheur.DeclencheurU(proba.Proba(1, True), "prieresPaiennesChretiennes")
        prieresPaiennesChretiennes.AjouterCondition(estPasRoi)
        selecteur_.ajouterDeclencheur(prieresPaiennesChretiennes)

label diviniteTutelaire:
    "Vous êtes à la foi prince et prêtre des dieux de votre peuple. Tous demandent des prières et des sacrifices et tous doivent être honorés."
    $ AjouterACarac(metier.Pretre.NOM, 1)
    menu:
        "Mais lequel est votre divinité tutélaire ?"
        "Wotan le sournois et changeant dieux des batailles":
            $ AjouterACarac(trait.Ruse.NOM, 1)
            $ AjouterACarac(metier.Stratege.NOM, 1)

        "Thor le redoutable maître du tonnerre":
            $ AjouterACarac(trait.Courage.NOM, 1)
            $ AjouterACarac(trait.Violence.NOM, 1)
            $ AjouterACarac(metier.Guerrier.NOM, 1)
            # $ AjouterACarac(metier.Chasseur.NOM, 1)

        "Freya, déesse de la fertilité et du désir charnel":
            # $ AjouterACarac(trait.Richesse.NOM, 1)
            $ AjouterACarac(trait.Altruisme.NOM, 1)
            $ AjouterACarac(metier.Politique.NOM, 1)

    jump fin_cycle

label prieresPaiennesChretiennes:
    # victoire et prières des païens et des chrétiens
    "Aujourd'hui vous avez remporté une grande victoire aux côté de votre père Chilpéric."
    $ AjouterACarac(clovis.Clovis.C_GLOIRE, 1)
    "Avec vos leudes, vos suivants, vous glorifiez Wotan dieu des batailles et priez pour que les Walkyries mènent vos guerriers tombés au combat jusqu'au Valhalla."
    "Vous remarquez alors un groupe de gaulois qui a combattu à vos côtés et qui semble prier à genoux à la manières des catholiques."
    menu:
        "Vous vous moquez de leur dieu faible et crucifié":
            "Vous raillez les chrétiens aussi faibles que leurs dieu. Ils n'osent pas répliquer au descendant des dieux que vous êtes et vont se cacher dans leur tente sans doute pour pleurnicher auprès de Jésus."
            "Vos guerriers rient de bon coeur. Ils sont fiers de vous avoir pour chef."
            $ RetirerACarac(clovis.Clovis.C_USURPATION, 1)
            $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 1)
            "Quand il en a vent votre père critique votre attitude : vous aurez besoin de l'appui des gaulois pour régner. Les insulter quand ils sont en plus de votre côté est une imprudence."
            $ RetirerACarac(clovis.Clovis.C_FIDELITE_GAULE, 1)
            jump fin_cycle
        "Vous vous intéressez à leurs prières.":
            "Vos guerriers apprécient peu votre attitude. Après tout pourquoi un descendant des dieux tels que vous s'intéresse-t'il à un dieu tout juste bon à se faire maltraiter."
            $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
            "Sans pour autant vous joindre à eux -vous ne parlez de toute façon pas leur langue- vous êtes néanmoins ébranlé par la ferveur tranquille des catholiques gaulois."
            $ AjouterACarac(clovis.Clovis.C_CHRISTIANISME, 1)
            jump fin_cycle
        "Vous les ignorez.":
            jump fin_cycle

    jump fin_cycle

label noyagePourAdultere:
    # intervention lors d'une noyade de femme adultère
    play music paien_sombre noloop
    "Alors que vous chassez en bordure des marais vous remarquez un attroupement d'où partent des pleurs et des cris."
    "En vous approchant vous ne voyez nul signe de violence mais une vingtaine de personnes au visage grave."
    "Une partie est en pleur. Parmi eux un homme jeune semble passer successiment de la rage au désespoir."
    "Vous comprenez quand vous remarquez le juge habillé en bourreau et la jeune femme attachée qui se tient devant lui : cette femme a sans doute commis un grand crime et va être noyée dans le marais selon la coutume franque."
    "Le moment est solennel et même un prince de sang royal tel que vous se doit de rester digne."
    menu:
        "Que faites vous ?"
        "Si vous intervenez pour demander des explications aux juges":
            "L'assemblée était si tendue que personne ne vous avait remarqué approcher."
            "Le juge vous informe que la jeune femme a été reconnue coupable d'adultère et va donc être exécutée par noyade."
            "La condamnée crie son innocence à votre intention mais un des garde la frappe et lui ordonne de faire preuve de plus de dignité. Elle se redresse la tête ensanglantée."
            menu:
                "Si vous demandez plus détails sur l'enquête et le procès.":
                    "Le juge s'impatiente et dit que l'adultère a été confirmé par trois témoins ici présents. Les témoins, une vieille femme et deux hommes, acquièscent."
                    menu:
                        "Si vous ordonnez l'interruption de l'exécution et une peine plus légère":
                            jump noyagePourAdultere_stop
                        "Si vous laissez l'exécution se poursuivre":
                            jump noyagePourAdultere_execution
                "Si vous ordonnez l'interruption de l'exécution et une peine plus légère":
                    jump noyagePourAdultere_stop
                "Si vous laissez l'exécution se poursuivre":
                    jump noyagePourAdultere_execution
        "Si vous laissez l'exécution se poursuivre":
            jump noyagePourAdultere_execution

    label noyagePourAdultere_stop:
        "Le juge est outré par votre intervention mais est bien obligé de se soumettre à l'autorité du prince prêtre."
        "La condamnée est relâchée et vous remercie en pleurant de bonheur. Le mari lui-même est soulagé et vous remercie."
        "Le regard des guerriers francs est par contre sans ambiguïté : ils méprisent l'homme trompé et prennent votre générosité pour de la faiblesse."
        $ AjouterACarac(clovis.Clovis.C_USURPATION, 1)
        jump fin_cycle

    label noyagePourAdultere_execution:
        "Le bourreau attache une pierre autour du cou de la condamnée et la pousse dans le marais."
        "Elle se débat quelques secondes puis sombre en se lamentant. L'assemblée jette alors diverses pierres et fagots là où elle est sombée pour que son corps reste sous l'eau par laquelle elle sombrera jusqu'aux enfers où est sa place."
        $ religionActuelle = situation_.GetValCarac(religion.Religion.C_RELIGION)
        if religionActuelle == religion.Christianisme.NOM:
            "Cette exécution païenne heurte durement vos sentiments catholiques."
            "Certes vous devez respecter les croyances et coutumes de votre peuple mais même l'âme des pécheurs mérite un peu plus de dignité."
            $ RetirerACarac(clovis.Clovis.C_CHRISTIANISME, 2)
            jump fin_cycle
        else:
            "Grâce à l'art du prêtre et au recueillement de l'assemblée cette dure coutume vous en apprend beaucoup sur la religion."
            $ AjouterACarac(metier.Pretre.NOM, 1)
        jump fin_cycle

    jump fin_cycle
